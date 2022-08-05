from flask import Blueprint, redirect, render_template, request, session, url_for
import re
from .decorators import *
from ..utils.database import *
from ..utils.solar import *
from ..utils.find_tutor import *
from ..utils.clean_str import *
from ..utils.validate_student import *


student = Blueprint("student",__name__, static_folder="static", template_folder="templates")


@student.route('/')
@login_required
def index():
    return render_template('student/index.html')


@student.route("/login")
def login():
    return render_template('student/login.html')


@student.route("/faq")
@login_required
def faq():
    return render_template('student/faq.html')


@student.route("/contact_with_us")
@login_required
def contact_with_us():
    return render_template('student/contact_with_us.html')


@student.route("/keywords")
@login_required
def keywords():
    return render_template('student/keywords.html')


@student.route("/suggest_question")
@login_required
def suggest_question():
    return render_template('student/suggest_question.html')


@student.route('/sending_email_contact', methods=["POST"])
@login_required
def sending_email_contact():
    return "ACTUALMENTE ESTAMOS EN MANTENIMIENTO"


@student.route('/sending_email_suggestion', methods=["POST"])
@login_required
def sending_email_suggestion():
    return "ACTUALMENTE ESTAMOS EN MANTENIMIENTO"


@student.route('/chatbot_student', methods=["POST"])
@login_required
def chatbotResponse():
    the_question = request.form['question']
    if request.method == 'POST' and the_question:
        if re.match("^[0-9]{9}$[ ]{0}", the_question):
            answer = Get_Tutor(the_question).find_tutor()
            result = Clean(answer).cleaned()
            return result
        answer = Question(the_question).find_answer()
        result = Clean(answer).cleaned()
        return result
    return result


@student.route('/verify', methods=["POST"])
def verify():
    studentCode = request.form['code']
    if request.method == 'POST' and studentCode and re.match("^[0-9]{9}$[ ]{0}", studentCode):
        result = Validate(studentCode)
        temp = result.validate_student()
        result = Clean(temp).cleaned()
        if studentCode == result.replace(" ",""):
            session['studentCode'] = studentCode
            session.permanent = True
            return redirect(url_for('student.index'))
    return redirect(url_for('student.login'))


@student.route('/logout')
def logout():
    session.pop('studentCode',None)
    session.permanent = False
    return redirect(url_for('home.index'))


@student.errorhandler(400)
def handle_bad_request(e):
    return render_template('errors/client/400.html'), 400


@student.errorhandler(403)
def handle_bad_request(e):
    return render_template('errors/client/400.html'), 403


@student.errorhandler(404)
def not_found(self):
    return render_template('errors/client/404.html'), 404


@student.errorhandler(405)
def method_not_found(error):
    return render_template('errors/client/405.html'), 405


@student.errorhandler(408)
def request_timeout(error):
    return render_template('errors/client/408.html'), 408


@student.errorhandler(410)
def page_gone(error):
    return render_template('errors/client/410.html'), 410


@student.errorhandler(500)
def internal_error(error):
    return render_template('errors/server/500.html'), 500


@student.errorhandler(505)
def http_not_compatible(error):
    return render_template('errors/server/500.html'), 505
