from flask import Flask, render_template

from blueprints.home import home_bp
from blueprints.about import about_bp
from blueprints.contact import contact_bp
from blueprints.cms import cms_bp


def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(cms_bp)

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    return app
