import smtplib
import imghdr
from email.message import EmailMessage


PASSWORD = "zbbh rmuw rxzh octh"
SENDER = "aaagrawal14@gmail.com"
RECIEVER = "aaagrawal14@gmail.com"


def send_email(image_path):
    print("send email started")
    email_message = EmailMessage()
    email_message["Subject"] = "Hey! something showed up..."
    email_message.set_content("There is something around here. plz check!")


    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="images", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECIEVER, email_message.as_string())
    gmail.quit()
    print("send email ended")


if __name__ == "__main__":
    send_email(image_path="images/19.png")