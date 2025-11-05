from flask import request
from app import create_app
import os

app = create_app()


@app.before_request
def check_login():
    return


if __name__ == "__main__":
    app.run(debug=True)
