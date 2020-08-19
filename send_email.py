import smtplib  
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import sys

SENDER_EMAIL = "collinsefe@gmail.com"
SENDER_NAME =  "collinsefe@gmail.com"



def main():
    RECIPIENT_EMAIL = sys.argv[1]
    SUBJECT = sys.argv[2]
    BODY_TEXT = sys.argv[3]
    LOCATION_OF_IMAGE = sys.argv[4]

    USERNAME_SMTP = "*************"
    PASSWORD_SMTP = "*************"

    HOST = "email-smtp.eu-west-2.amazonaws.com"
    PORT = 587

    BODY_HTML = """<html>
                <head></head>
                    <body>
                        <h1>This is a test </h1>
                        <p>this is a test message</p>
                    </body>
                </html>
            """
    if len(sys.argv) > 3:
        fp = open(LOCATION_OF_IMAGE, 'rb')
        image = MIMEImage(fp.read(),_subtype="svg")
        fp.close()
        image.add_header('Content-Disposition', 'attachment', filename='output.svg')
    

    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = email.utils.formataddr((SENDER_NAME, SENDER_EMAIL))
    msg['To'] = RECIPIENT_EMAIL

    part1 = MIMEText(BODY_TEXT, 'plain')
    part2 = MIMEText(BODY_HTML, 'html')
    msg.attach(part1)
    msg.attach(part2)

    if len(sys.argv) > 3:
        msg.attach(image)

    try:  
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        #stmplib docs recommend calling ehlo() before & after starttls()
        server.ehlo()
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        server.sendmail(SENDER_NAME, RECIPIENT_EMAIL, msg.as_string())
        server.close()
    # Display an error message if something goes wrong.
    except Exception as e:
        print ("Error: ", e)
    else:
        print ("Email sent!")





if __name__ == "__main__":
    main()