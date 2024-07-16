from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired

#Форма для регистрации
class RegisterForm(FlaskForm):
    name = StringField(label="Имя", validators=[DataRequired("Введите имя")])
    email = EmailField(label="Почта", validators=[DataRequired("Введите почту")])
    password = PasswordField(label="Пароль",
                             validators=[DataRequired("Введите пароль")])
    password_repeat = PasswordField(label="Повторите пароль",
                                    validators=[DataRequired("Повторите пароль")])
    button = SubmitField(label="Зарегистрироваться")
class LoginForm(FlaskForm):
    email = EmailField(label="Почта", validators=[DataRequired("Введите почту")])
    password = PasswordField(label="Пароль",
                             validators=[DataRequired("Введите пароль")])
    button = SubmitField(label="Войти")