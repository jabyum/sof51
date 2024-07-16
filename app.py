from flask import Flask
from users import user_bp
from questions import question_bp
app = Flask(__name__)
# регистрация блюпринтов
app.register_blueprint(user_bp)
app.register_blueprint(question_bp)
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = '2u454u23909024r50u9'
@app.route("/")
def home():
    user_link = "<a href='/user'>Юзеры</a><br>"
    question_link = "<a href='/question'>Вопросы</a><br>"
    return user_link + question_link

app.run(debug=True)
