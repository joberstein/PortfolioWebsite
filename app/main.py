from flask import Flask

from app.home import home_page
from app.about import about_page
from app.portfolio import portfolio_page
from app.contact import contact_page

app = Flask(__name__)

app.register_blueprint(home_page)
app.register_blueprint(about_page)
app.register_blueprint(portfolio_page)
app.register_blueprint(contact_page)

if __name__ == "__main__":
    app.debug=True
    app.host="localhost"
    app.run()