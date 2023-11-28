import smtplib
import threading
from datetime import datetime
from email.mime.text import MIMEText
from constants import Constants


class Notifier:
    def __init__(self, credentials: dict, receipients: list[str], url, is_test=False):
        self.username = credentials["username"]
        self.password = credentials["password"]
        self.recipients = receipients
        self.url = url
        self.time_start = datetime.now()
        self.hcheck_thread = threading.Thread(target=self.health_check)
        self.hcheck_thread.start()
        self.hcheck_sent_today = False
        self.is_test = is_test

    def notify(self, date):
        self.send_email(Constants.subject, Constants.body1 + date + Constants.body2 + self.url)

    def health_check(self):
        while datetime.now() < Constants.end_date:
            days_elapsed = self.time_start.day - datetime.now().day
            if days_elapsed % 3 == 0 and not self.hcheck_sent_today:
                if self.is_test:
                    print("health check")
                else:
                    self.send_email("Health Check", "Health Check")
                self.hcheck_sent_today = True
            elif days_elapsed % 3 != 0:
                self.hcheck_sent_today = False


    def send_email(self, subject, body):
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = self.username
        print(self.recipients[0])
        msg["To"] = ', '.join(self.recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(self.username, self.password)
            smtp_server.sendmail(self.username, self.recipients, msg.as_string())
        print("Message sent!")
