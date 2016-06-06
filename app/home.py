from flask import render_template, Blueprint

home_page = Blueprint('home_page', __name__)


@home_page.route("/", methods=["GET"])
def home():
    return render_template("pages/home.html")