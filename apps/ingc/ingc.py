from flask import Blueprint, redirect, render_template, request, session, url_for
from datetime import timedelta
import re
from .decorators import *
from ..utils.database import *
from .controlator import *


ingc = Blueprint("ingc",__name__, static_folder="static", template_folder="templates")


@ingc.route('/')
@login_required
def index():
    return render_template('ingc/index.html')


@ingc.route("/login")
def login():
    return render_template('ingc/login.html')


@ingc.route("/faq")
@login_required
def faq():
    return render_template('ingc/faq.html')


@ingc.route("/contact_with_us")
@login_required
def contact_with_us():
    return render_template('ingc/contact_with_us.html')


@ingc.route("/keywords")
@login_required
def keywords():
    return render_template('ingc/keywords.html')


@ingc.route("/suggest_question")
@login_required
def suggest_question():
    return render_template('ingc/suggest_question.html')


@ingc.route('/sending_email_contact', methods=["POST"])
@login_required
def sending_email_contact():
    return "ACTUALMENTE ESTAMOS EN MANTENIMIENTO"


@ingc.route('/sending_email_suggestion', methods=["POST"])
@login_required
def sending_email_suggestion():
    return "ACTUALMENTE ESTAMOS EN MANTENIMIENTO"


@ingc.route('/chatbot_ingc', methods=["POST"])
@login_required
def chatbotResponse():
    the_question = request.form['question']
    if request.method == 'POST' and the_question:
        if re.match("^[0-9]{9}$[ ]{0}", the_question):
            answer = find_tutor(the_question)
            if type(answer) is tuple:
                result = delete_special_characters(answer)
                return result
            return answer
        else:
            answer = find_answer(the_question)
            if type(answer) is tuple:
                result = delete_special_characters(answer)
                return result
    return answer


@ingc.route('/verify', methods=["POST"])
def verify():
    studentCode = request.form['code']
    if request.method == 'POST' and studentCode and re.match("^[0-9]{9}$[ ]{0}", studentCode):
        result = validate_student(studentCode)
        if studentCode == result:
            session['studentCode'] = studentCode
            session.permanent = True
            ingc.permanent_session_lifetime = timedelta(minutes=120)
            return redirect(url_for('ingc.index'))
    return redirect(url_for('ingc.login'))


@ingc.route('/logout')
def logout():
    session.pop('studentCode',None)
    session.permanent = False
    return redirect(url_for('ingc.login'))


@ingc.errorhandler(400)
def handle_bad_request(e):
    return render_template('errors/client/400.html'), 400


@ingc.errorhandler(403)
def handle_bad_request(e):
    return render_template('errors/client/400.html'), 403


@ingc.errorhandler(404)
def not_found(self):
    return render_template('errors/client/404.html'), 404


@ingc.errorhandler(405)
def method_not_found(error):
    return render_template('errors/client/405.html'), 405


@ingc.errorhandler(408)
def request_timeout(error):
    return render_template('errors/client/408.html'), 408


@ingc.errorhandler(410)
def page_gone(error):
    return render_template('errors/client/410.html'), 410


@ingc.errorhandler(500)
def internal_error(error):
    return render_template('errors/server/500.html'), 500


@ingc.errorhandler(505)
def http_not_compatible(error):
    return render_template('errors/server/500.html'), 505
