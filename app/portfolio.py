from flask import render_template, Blueprint, current_app
import json, base64

portfolio_page = Blueprint("portfolio_page", __name__)


@portfolio_page.route("/portfolio", methods=["GET"])
def portfolio():
    return render_template("pages/portfolio.html")


@portfolio_page.route("/portfolio/<section>", methods=["GET"])
def portfolio_section(section):
    with current_app.open_resource("static/json/portfolio/" + section + ".json") as file:
        contents = file.read()
        # stringy = file.decode("utf-8")
        json_response = json.loads(contents.decode('utf-8'))
        print(json_response)
        return render_template("pages/portfolio-section.html")