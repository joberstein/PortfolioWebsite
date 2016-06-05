from flask import Flask, request, render_template
import smtplib
app = Flask(__name__)


@app.route("/portfolio", methods=["GET"])
def portfolio():
    return render_template("portfolio.html")