import os

from dotenv import load_dotenv
from flask import Flask

from app.routes import register_routes

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    ##Registtrando rota de erro para toda a aplicação
    register_routes(app)
    from .routes.error_handler_route import error_bp

    app.register_blueprint(error_bp)

    return app
