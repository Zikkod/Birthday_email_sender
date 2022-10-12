import time
from login import getlogin, getpassword
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from log import log
from getmessagetemplate import getmessagetemplate
from checkdb import checkdb


def sendmail():
    """This function makes the mailing of congratulations to people in sendlist"""

    sender = getlogin()  # Your email address
    password = getpassword()  # Your app password

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Your mail server
        server.starttls()  # Start encryption
        log("Connected to server")

        server.login(sender, password)
        log("Successful logged in")

        sendlist = checkdb()
        log("Sendlist is ready")

        messagetemplate = getmessagetemplate()

        if messagetemplate != "Error:Couldn't get a message template":
            for name, email in sendlist:
                try:
                    """msg = MIMEText(messagetemplate.format(name), 'html') for html letter or
                     or msg = MIMEText(messagetemplate.format(name),, 'plain') for regular letter
                     """
                    msg = MIMEText(messagetemplate.format(name), 'html')  # Your congratulation
                    msg["Subject"] = Header(f"Happy birthday, {name}!", 'utf-8')
                    msg['From'] = sender
                    msg['To'] = name
                    server.sendmail(sender, email, msg.as_string())
                    log(f"Email sent successfully to {email}")
                except Exception:
                    log(f"Failed sending email to {email}")
                time.sleep(3)  # Delay between sending
            else:
                log("Couldn't get a message template")
    except Exception as _ex:
        log(f"Connection to mail server failed\n{_ex}")
    return "End of mailing"
