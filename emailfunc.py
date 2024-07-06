import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, content):
    try:
        # SMTP sunucusuna bağlanma
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.starttls()
        mail.login(sender_email, sender_password)

        # E-posta oluşturma
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # E-posta içeriği eklemek
        message.attach(MIMEText(content, 'plain'))

        # E-postayı gönderme
        mail.sendmail(sender_email, recipient_email, message.as_string())

        # SMTP bağlantısını kapatma
        mail.quit()

        print("E-posta başarıyla gönderildi.")
    except Exception as e:
        print(f"E-posta gönderilirken bir hata oluştu: {e}")

