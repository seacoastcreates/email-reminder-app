from temporalio import activity
import smtplib
from email.message import EmailMessage

@activity.defn
async def send_email_activity(email: str):
    # Simulate sending an email
    print(f"Sending email to {email}")
    # Here you would integrate with an actual email service
    return f"Email sent to {email}"