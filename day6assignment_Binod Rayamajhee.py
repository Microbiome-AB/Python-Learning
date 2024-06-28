#Create a QR Code Generator That Sends an Email to a User

#Title: My First Email Using Python

#Body: Hello, this is my first email using Python

send_email(
    subject="My First Email Using Python",
    body="Hello, this is my first email using Python",
    to_email="recipient@example.com",
    from_email="your_email@example.com",
    smtp_server="smtp.example.com",
    smtp_port=587,
    smtp_user="your_email@example.com",
    smtp_password="your_password",
    attachment_path="email_qr.png"
)