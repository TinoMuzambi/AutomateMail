import smtplib
import time

def sendMail(from_email, from_email_password, email_subject, email_body, to_email):
    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(from_email, from_email_password)

    message = "Subject: {}\n\n{}".format(email_subject, email_body)

    server.sendmail(from_email, to_email, message)

    server.quit()

def main():
    count = 1 # Counter for keeping track of number of emails sent.
    while True:
        count += 1
        from_email = '' # Email address email is being sent from.
        from_email_password = '' # Password of email account email is being sent from.
        email_subject = '' # Subject of the email to be sent.
        email_body = '' # Body of the email to be sent.
        to_email = '' # Email address email is being sent to.
        sendMail(from_email, from_email_password, email_subject, email_body, to_email)
        print('Sent ' + str(count))
        time.sleep(5)

if __name__=="__main__":
    main()