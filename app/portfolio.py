from flask import render_template, Blueprint, current_app
import json, base64

portfolio_page = Blueprint("portfolio_page", __name__)


@portfolio_page.route("/portfolio", methods=["GET"])
def portfolio():
    return render_template("pages/portfolio.html")


@portfolio_page.route("/portfolio/<section>", methods=["GET"])
def portfolio_section(section):
    json_response = get_json_file_contents("static/json/portfolio/" + section + ".json")
    return render_template("pages/portfolio-section.html", section_name=section, portfolio_pieces=json_response)


@portfolio_page.route("/portfolio/<section>/<int:index>", methods=["GET"])
def portfolio_piece(section, index):
    json_response = get_json_file_contents("static/json/portfolio/" + section + ".json")
    piece=json_response[index]
    return render_template("fragments/_portfolio-piece.html", section_name=section, piece=piece)


def get_json_file_contents(filepath):
    with current_app.open_resource(filepath) as file:
        contents = file.read()
        return json.loads(contents.decode('utf-8'))