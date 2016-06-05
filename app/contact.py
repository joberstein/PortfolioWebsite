import base64
from email.mime.text import MIMEText

import httplib2
from flask import Flask, request, render_template
from flask.ext.mail import Message, Mail
from oauth2client import client
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
from httplib2 import Http
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow

mail = Mail()
app = Flask(__name__)

scopes = ['https://www.googleapis.com/auth/gmail.compose']
credentials = ServiceAccountCredentials.from_json_keyfile_name('static/json/keyfile.json', scopes=scopes)
delegated_credentials = credentials.create_delegated('admin@jesseoberstein.com')
http_auth = delegated_credentials.authorize(Http())
gmail_service = build('gmail', 'v1', http=http_auth)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", pageName="contact", formStatus="VIEWED")

    elif request.method == "POST":
        name = request.form["name"]
        sender = request.form["email"]
        message_body = request.form["message"]
        human = request.form["human"]

        message = MIMEText("From: " + name + "\n" + "Email: " + sender + "\n\n" + message_body)
        message['to'] = "oberstein.j@husky.neu.edu"
        message['from'] = "admin@jesseoberstein.com"
        message['subject'] = "My Portfolio - Contact Form Message"
        request_body = {'raw': str(base64.urlsafe_b64encode(message.as_string().encode("utf-8")), "utf-8")}

        return send_message(request_body, not human)


def send_message(request_body, human):
    if human:
        try:
            gmail_service.users().messages().send(userId="me", body=request_body).execute()
        except Exception as error:
            print('An error occurred: %s' % error)
            return render_template("contact.html", pageName="contact", formStatus="FAILED")

    return render_template("contact.html", pageName="contact", formStatus="SENT")


if __name__ == "__main__":
    app.debug=True
    app.host="localhost"
    app.run()