import smtplib
import time
import sys


def send_mail(from_email, from_email_password, email_subject, email_body, to_email):
    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(from_email, from_email_password)

    message = "Subject: {}\n\n{}".format(email_subject, email_body)

    server.sendmail(from_email, to_email, message)

    server.quit()


def main():
    count = 0  # Counter for keeping track of number of emails sent.
    from_email = sys.argv[1]  # Email address email is being sent from.
    from_email_password = sys.argv[2]  # Password of email account email is being sent from.
    email_subject = sys.argv[3]  # Subject of the email to be sent.
    email_body = sys.argv[4]  # Body of the email to be sent.
    to_email = sys.argv[5]  # Email address email is being sent to.

    while True:
        count += 1
        send_mail(from_email, from_email_password, email_subject, email_body, to_email)
        print('Sent ' + str(count))
        time.sleep(5)  # Change this to change the interval between sending email.


if __name__ == "__main__":
    main()
