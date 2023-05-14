import smtplib
import getpass

smtp = smtplib.SMTP('smtp.gmail.com', 587)
print(f'EHLO: {smtp.ehlo()}')
print(f'Start TLS: {smtp.starttls()}')

email = input('User: ')
password = getpass.getpass('Password: ')
print(f'Login: {smtp.login(email, password)}')

subject = input('Subject: ')
message = input('Message: ')

result = smtp.sendmail(from_addr=email, to_addrs=email,
                       msg=f'Subject: {subject}\n{message}')
