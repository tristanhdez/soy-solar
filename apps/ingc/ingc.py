from flask import Blueprint, redirect, render_template, jsonify, request, session, url_for
from datetime import timedelta
import apps.ingc.processor_ingc as processor_ingc
import re
from .decorators import *
from ..utils.database import *


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


@ingc.route("/suggest_question")
@login_required
def suggest_question():
    return render_template('ingc/suggest_question.html')


@ingc.route('/sending_email_contact', methods=["POST"])
@login_required
def sending_email_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    if request.method == 'POST' and name and email and message:
        return "ACTUALMENTE ESTAMOS EN MANTENIMIENTO"


@ingc.route('/sending_email_suggestion', methods=["POST"])
@login_required
def sending_email_suggestion():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    if request.method == 'POST' and name and email and message:
        return "ACTUALMENTE ESTAMOS EN MANTENIMIENTO"


@ingc.route('/chatbot_ingc', methods=["POST"])
@login_required
def chatbotResponse():
    if request.method == 'POST':
        the_question = request.form['question']
        if re.match("^[0-9]{9}$", the_question):
            connection = mysql.connect()
            cursor=connection.cursor()
            row = cursor.execute("SELECT tutors.name, tutors.email from tutors join students on tutors.id_tutor = students.id_tutor where students.code = '"+the_question+"'")
            connection.commit()
            data = cursor.fetchall()
            if row == 1:
                result = " ".join(str(x) for x in data)
                result = result.replace("(","").replace(")","").replace("'","").replace("\\n"," ").replace("\\r"," ").replace("\\"," ")
                result = result.replace(","," ")
                return result
        response = processor_ingc.chatbot_response(the_question)
    return jsonify({"response": response })


@ingc.route('/verify', methods=["POST"])
def verify():
    studentCode = request.form['code']
    if request.method == 'POST' and studentCode and re.match("^[0-9]{9}$[ ]{0}", studentCode):
        connection = mysql.connect()
        cursor=connection.cursor()
        cursor.execute("SELECT code FROM students WHERE code='"+studentCode+"'")
        connection.commit()
        data = cursor.fetchall()
        result = " ".join(str(x) for x in data)
        result = result.replace("(","").replace(")","").replace(","," ").replace(" ","")
        if studentCode == result:
            cursor.execute("SELECT name FROM students WHERE code='"+studentCode+"'")
            connection.commit()
            name = cursor.fetchall()
            cursor.close()
            value = " ".join(str(x) for x in name)
            value = value.replace("(","").replace(")","").replace(","," ").replace("'","")
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