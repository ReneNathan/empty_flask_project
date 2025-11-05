from dotenv import load_dotenv
from flask import Flask, Blueprint, render_template

load_dotenv()

app = Flask(__name__)

home_bp = Blueprint(
    "home_bp",
    __name__,
    url_prefix="/",
)


@home_bp.route("/")
def home():
    return render_template("home/home.html")
