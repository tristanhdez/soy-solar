from flask import Blueprint, redirect, render_template, jsonify, request, session, url_for
from datetime import timedelta
import apps.ingc.processor_ingc as processor_ingc
import re
from .decorators import *


ingc = Blueprint("ingc",__name__, static_folder="static", template_folder="templates")


@ingc.route('/')
@login_required
def index():
    return render_template('ingc/index.html')


@ingc.route("/login")
def login():
    return render_template('ingc/login.html')


@ingc.route('/chatbot_ingc', methods=["POST"])
@login_required
def chatbotResponse():
    if request.method == 'POST':
        the_question = request.form['question']
        response = processor_ingc.chatbot_response(the_question)
    return jsonify({"response": response })


@ingc.route('/verify', methods=["POST"])
def verify():
    studentCode = request.form['code']
    if studentCode and re.match("^[0-9]{9}$[ ]{0}", studentCode) and request.method == 'POST':
        session['studentCode'] = studentCode
        session.permanent = True
        ingc.permanent_session_lifetime = timedelta(minutes=120)
        return redirect(url_for('ingc.index'))
        #connection = mysql.connect()
        #cursor=connection.cursor()
        #cursor.execute("SELECT codigo FROM alumnos WHERE codigo='"+studentCode+"'")
        #connection.commit()
        #data = cursor.fetchall()
        #result = " ".join(str(x) for x in data)
        #result = result.replace("(","").replace(")","").replace(","," ").replace(" ","")
        #if studentCode == result:
        #    connection = mysql.connect()
        #    cursor=connection.cursor()
        #    cursor.execute("SELECT nombre FROM alumnos WHERE codigo='"+studentCode+"'")
        #    connection.commit()
        #    name = cursor.fetchall()
        #    value = " ".join(str(x) for x in name)
        #    value = value.replace("(","").replace(")","").replace(","," ").replace("'","")
        #   session['studentCode'] = studentCode
        #    session.permanent = True
        #    app.permanent_session_lifetime = timedelta(minutes=120)
        #    return redirect('/solar')
    return redirect(url_for('ingc.login'))


@ingc.route('/logout')
def logout():
    session.pop('studentCode',None)
    session.permanent = False
    return redirect(url_for('ingc.login'))
