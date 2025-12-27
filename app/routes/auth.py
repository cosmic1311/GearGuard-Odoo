from flask import Blueprint, render_template, request, redirect, url_for , flash 
from flask_login import login_user
from app import db
from werkzeug.security import generate_password_hash , check_password_hash
from app.models import User


auth_bp = Blueprint('auth', __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()

        if user and check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("dashboard.dashboard"))

        flash("Invalid username or password", "danger")

    return render_template("login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("auth.register"))

        user = User(
            username=username,
            password=generate_password_hash(password)
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.login"))

    return render_template("register.html")