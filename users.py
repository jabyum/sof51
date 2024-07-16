from flask import Blueprint, render_template
from forms import LoginForm, RegisterForm
user_bp = Blueprint("users", __name__, url_prefix="/user")

@user_bp.route("/")
def user():
    register_link = "<a href='/user/registration'>Регистрация</a><br>"
    login_link = "<a href='/user/login'>Войти в аккаунт</a><br>"
    return register_link + login_link
@user_bp.route("/registration")
def registration():
    form = RegisterForm()
    return render_template("register.html", form=form)
@user_bp.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

