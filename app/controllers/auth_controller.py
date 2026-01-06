from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from ..services.auth_service import register_user, find_user_by_email


def show_login():
    return render_template("auth/login.html")


def login_action():
    email = request.form.get("email")
    password = request.form.get("password")

    user = find_user_by_email(email)

    if not user or not user.check_password(password):
        flash("Invalid credentials")
        return redirect(url_for("auth.login"))

    login_user(user)
    return redirect(url_for("auth.login"))


def show_register():
    return render_template("auth/register.html")


def register_action():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        register_user(username, email, password)
        flash("Registered successfully — login now.")
        return redirect(url_for("auth.login"))
    except ValueError as e:
        flash(str(e))
        return redirect(url_for("auth.register"))


def logout_action():
    logout_user()
    return redirect(url_for("auth.login"))
