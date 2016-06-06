from flask import render_template, Blueprint

about_page = Blueprint("about_page", __name__)


@about_page.route("/about", methods=["GET"])
def about():
    return render_template("pages/about.html")