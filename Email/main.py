import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Dave RObertson'
email['to'] = 'davidmacrobertson@gmail.com'
