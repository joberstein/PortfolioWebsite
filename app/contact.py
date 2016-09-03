from flask import request, render_template, Blueprint, Flask, json
from smtplib import SMTPException
from flask.ext.mail import Mail, Message
from validate_email import validate_email
from app.form_status import FormStatus

JESSE_EMAIL = "joberstein12@gmail.com"
NEW_MESSAGE_SUBJECT = "My Portfolio - Contact Form Message"
RECEIPT_MESSAGE_SUBJECT = "Message Sent to Jesse Oberstein"

contact_page = Blueprint('contact_page', __name__)
app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = JESSE_EMAIL
app.config['MAIL_DEFAULT_SENDER'] = JESSE_EMAIL

with app.open_resource('static/json/security/app-secure-pass.json') as file:
    data = json.load(file)
    app.config['MAIL_PASSWORD'] = data["portfolio-website"]

mail = Mail(app)
auto_save= Message("", sender=JESSE_EMAIL, recipients=[JESSE_EMAIL], body="")


@contact_page.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("pages/contact.html", FormStatusEnum=FormStatus, formStatus=FormStatus.VIEWED, autoSave=auto_save)

    elif request.method == "POST":
        # Gather input fields from contact form
        name = request.form["name"]
        sender = request.form["email"]
        body = request.form["message"]
        is_robot = request.form["human"]
        is_valid_sender = validate_email(sender)

        # Assemble a message from the contact form input to send to me.
        message_body = "From: {0}\n" \
                       "Email: {1}\n\n" \
                       "{2}".format(name, sender, body)
        message = compose_message(sender, [JESSE_EMAIL], NEW_MESSAGE_SUBJECT, message_body)

        # Assemble a message from the contact form input to send to the sender as a receipt.
        receipt_message_body = "Hi {0},\n\n" \
                               "You sent the following message to Jesse Oberstein via his website at " \
                               "www.jesseoberstein.com/contact:\n\n" \
                               "{1}".format(name, body)
        receipt_message = compose_message(JESSE_EMAIL, [sender], RECEIPT_MESSAGE_SUBJECT, receipt_message_body)

        auto_save.body = body
        return send_messages([message, receipt_message], is_robot, is_valid_sender)


# Assemble a message object
def compose_message(from_email, recipients, subject, body):
    message = Message(subject, sender=from_email, recipients=recipients)
    message.body = body
    return message


# Only send the provided message if the sender is human.  Otherwise, indicate the message has sent, but don't actually
# send the message to fool spambots.
def send_messages(messages, is_robot, is_valid_sender):
    if not is_robot:
        try:
            if not is_valid_sender:
                return render_template("pages/contact.html", FormStatusEnum=FormStatus, formStatus=FormStatus.FAILED, autoSave=auto_save)
            for msg in messages:
                mail.send(msg)

        except SMTPException:
            return render_template("pages/contact.html", FormStatusEnum=FormStatus, formStatus=FormStatus.FAILED, autoSave=auto_save)

    auto_save.body = ""
    return render_template("pages/contact.html", FormStatusEnum=FormStatus, formStatus=FormStatus.SENT, autoSave=auto_save)