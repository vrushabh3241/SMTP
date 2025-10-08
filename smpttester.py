import smtplib
import os
from email.message import EmailMessage

def send_email():
    """
    Connects to Gmail's SMTP server and sends a test email.
    Credentials and recipient are loaded from environment variables for security.
    """
  
    sender_email = os.getenv('MY_GMAIL_ADDRESS')
    app_password = os.getenv('MY_GMAIL_APP_PASSWORD')
    recipient_email = "recipient email address"  

  
    if not sender_email or not app_password:
        print("🔴 Error: Set the MY_GMAIL_ADDRESS and MY_GMAIL_APP_PASSWORD environment variables.")
        return

   
    msg = EmailMessage()
    msg['Subject'] = 'SMTP Test from Python'
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg.set_content('this is to test the working of SMTP server!')

 
    print(f"Sending email to {recipient_email}...")
    try:
        
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()  # Secure the connection
            smtp.login(sender_email, app_password)  # Log in using your App Password
            smtp.send_message(msg)  # Send the email
        
        print("✅ Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email or App Password.")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":

    send_email()

