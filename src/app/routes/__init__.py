from flask import Flask

from app.routes.first_route import home_bp

__all__ = ["register_routes"]


def register_routes(app: Flask):
    app.register_blueprint(home_bp)
