import smtplib
import time


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
    from_email = input("Enter the email address you wanna send the email from:\n")
    from_email_password = input("Enter the password of that email addresss:\n")
    email_subject = input("Enter the subject of the email:\n")
    email_body = input("Enter the body of the email:\n")
    to_email = input("Enter the email address you wanna send the email to:\n")

    while True:
        count += 1
        send_mail(from_email, from_email_password, email_subject, email_body, to_email)
        print('Sent ' + str(count))
        time.sleep(5)  # Change this to change the interval between sending email.


if __name__ == "__main__":
    main()
