from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib


def send(from_addr:str, from_pass:str, to: str, subject:str, imgPath:str, firm:str=None):
    try:
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = subject
        msgRoot['From'] = from_addr
        msgRoot['To'] = to

        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        html = '<img src="cid:image1">'
        if firm != None:
            html = html + '<br>' + firm
        msgText = MIMEText(html, 'html')
        msgAlternative.attach(msgText)

        fp = open(imgPath, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_addr, 'c1a2m3b4a5')
        server.sendmail(from_addr, to, msgRoot.as_string())
        server.quit()
        return True
    except:
        return False