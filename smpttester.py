import smtplib
import os
from email.message import EmailMessage

def send_email():
    """
    Connects to Gmail's SMTP server and sends a test email.
    Credentials and recipient are loaded from environment variables for security.
    """
    # 1. Load your credentials securely from environment variables
    sender_email = os.getenv('MY_GMAIL_ADDRESS')
    app_password = os.getenv('MY_GMAIL_APP_PASSWORD')
    recipient_email = "suhani.mishra1802@gmail.com"  # You can also load this from an env variable

    # Check if the environment variables are set correctly
    if not sender_email or not app_password:
        print("🔴 Error: Set the MY_GMAIL_ADDRESS and MY_GMAIL_APP_PASSWORD environment variables.")
        return

    # 2. Create the email content
    msg = EmailMessage()
    msg['Subject'] = 'SMTP Test from Python'
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg.set_content('abhi hoga system hack!')

    # 3. Send the email via Gmail's SMTP server
    print(f"Sending email to {recipient_email}...")
    try:
        # Establish a connection to the server on port 587
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()  # Secure the connection
            smtp.login(sender_email, app_password)  # Log in using your App Password
            smtp.send_message(msg)  # Send the email
        
        print("✅ Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email or App Password.")
    except Exception as e:
        print(f"An error occurred: {e}")


# This block makes the script runnable
if __name__ == "__main__":
    send_email()