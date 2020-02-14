import smtplib, ssl
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):


    port = 465  # For SSL
    sender_email = "steffen.knoedler.dev@gmail.com"
    receiver_email = "st.knoedler@gmail.com"
    password = "********"
    message = f"<h3> New Submission </h3><ul><li> Contact Person: {customer}</li><li>Reason: {dealer}</li><li> Urgency: {rating}</li><li> Message: {comments}</li></ul>"

    msg = MIMEText(message, 'html')
    msg['Subject'] = 'App Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Create a secure SSL context
    context = ssl.create_default_context()

    # send email
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("Steffen.knoedler.dev@gmail.com", password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
