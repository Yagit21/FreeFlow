from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User


auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        #If all fields are valid
        if not username or not email or not password:

            flash("Please fill in all fields.")

            return redirect(url_for("auth.signup"))

        if password != confirm_password:

            flash("Passwords do not match.")

            return redirect(url_for("auth.signup"))

        #Check whether username already exists
        existing_username = User.query.filter_by(username=username).first()

        if existing_username:
            flash("Username already exists.")
            return redirect(url_for("auth.signup"))

        #Check whether email already exists
        existing_email = User.query.filter_by(email=email).first()

        if existing_email:
            flash("Email already exists.")
            return redirect(url_for("auth.signup"))

        #Hash the password
        password_hash = generate_password_hash(password)

        #Create user
        new_user = User(username=username, email=email, password_hash=password_hash)

        #Save user
        db.session.add(new_user)
        db.session.commit()

        flash("Account successfully created.")

        return redirect(url_for("auth.login"))

    return render_template("signup.html")


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")

        password = request.form.get("password")

        #Find user by email
        user = User.query.filter_by(email=email).first()

        #Check user exists and password is correct
        if user and check_password_hash(user.password_hash, password):

            #Store the user's ID in the session
            session["user_id"] = user.id
            session["username"] = user.username
            flash("Logged in successfully.")

            return redirect(url_for("routes.index"))

        flash("Incorrect email or password.")

    return render_template("login.html")


@auth.route("/logout")
def logout():

    session.pop("user_id", None)
    session.pop("username", None)

    flash("You have been logged out.")

    return redirect(url_for("routes.index"))