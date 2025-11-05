from flask import Blueprint, render_template, redirect, url_for

error_bp = Blueprint("main", __name__)


@error_bp.app_errorhandler(404)
def page_not_found(e):

    return (
        render_template("errors/generic_404.html"),
        404,
    )
