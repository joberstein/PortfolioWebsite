from flask import Flask, render_template

app = Flask(__name__)


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")