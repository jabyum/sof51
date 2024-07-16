from flask import Blueprint

question_bp = Blueprint("questions", __name__,
                        url_prefix="/question")

@question_bp.route('/')
def question():
    return "Hello from question"
