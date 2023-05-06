

import pandas as pd
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# 读取 Excel 文件
df = pd.read_excel('data.xlsx')

# 检查今天是否有更改的数据
today = datetime.today().strftime('%Y-%m-%d')
today_data = df[df['日期'] == today]

if not today_data.empty:
    # 发送邮件
    sender_email = 'your_email@example.com'
    receiver_email = 'recipient@example.com'
    password = 'your_password'

    message = MIMEText('今天有新的数据更新，请查收！')
    message['Subject'] = '数据更新通知'
    message['From'] = sender_email
    message['To'] = receiver_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())




