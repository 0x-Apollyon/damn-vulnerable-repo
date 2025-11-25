import smtplib

EMAIL = "apollyon@national.shitposting.agency"
PASSWORD = "oh_not_not_my_password"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587

try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.ehlo()

    server.starttls()
    server.ehlo()

    server.login(EMAIL, PASSWORD)

    print("Logged in successfully!")

finally:
    server.quit()
