import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Gmail hesabınızın bilgileri
email_gonderen = "gonderen@gmail.com"
sifre = "gonderenin_sifresi"

# E-posta bilgileri
email_alici = "alici@gmail.com"
konu = "Python ile e-posta gönderme"
icerik = "Merhaba, bu bir test e-postasıdır."

# SMTP sunucusuna bağlanma
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.starttls()
mail.login(email_gonderen, sifre)

# E-posta oluşturma
mesaj = MIMEMultipart()
mesaj['From'] = email_gonderen
mesaj['To'] = email_alici
mesaj['Subject'] = konu

# E-posta içeriği eklemek
mesaj.attach(MIMEText(icerik, 'plain'))

# E-postayı gönderme
mail.sendmail(email_gonderen, email_alici, mesaj.as_string())

# SMTP bağlantısını kapatma
mail.quit()

print("E-posta başarıyla gönderildi.")
