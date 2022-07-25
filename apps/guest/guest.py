from flask import Blueprint, render_template, request
from .controlator import *


guest = Blueprint("guest",__name__, static_folder="static", template_folder="templates")


@guest.route("/")
def index():
    return render_template('guest/index.html')


@guest.route('/chatbot_student', methods=["POST"])
def chatbotResponse():
    the_question = request.form['question']
    if request.method == 'POST' and the_question:
        answer = find_answer(the_question)
    if type(answer) is tuple:
        result = delete_special_characters(answer)
        return result
    return answer
    

@guest.route("/faq")
def faq():
    return render_template('guest/faq.html')


@guest.route("/keywords")
def keywords():
    return render_template('guest/keywords.html')


@guest.errorhandler(400)
def handle_bad_request(e):
    return render_template('errors/client/400.html'), 400


@guest.errorhandler(403)
def handle_bad_request(error):
    return render_template('errors/client/400.html'), 403


@guest.errorhandler(404)
def not_found(error):
    return render_template('errors/client/404.html'), 404


@guest.errorhandler(405)
def method_not_found(error):
    return render_template('errors/client/405.html'), 405


@guest.errorhandler(408)
def request_timeout(error):
    return render_template('errors/client/408.html'), 408


@guest.errorhandler(410)
def page_gone(error):
    return render_template('errors/client/410.html'), 410


@guest.errorhandler(500)
def internal_error(error):
    return render_template('errors/server/500.html'), 500


@guest.errorhandler(505)
def http_not_compatible(error):
    return render_template('errors/server/500.html'), 505
