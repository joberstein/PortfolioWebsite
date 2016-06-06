from flask import render_template, Blueprint

portfolio_page = Blueprint("portfolio_page", __name__)


@portfolio_page.route("/portfolio", methods=["GET"])
def portfolio():
    return render_template("pages/portfolio.html")