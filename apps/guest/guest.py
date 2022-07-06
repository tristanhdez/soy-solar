from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
import apps.guest.processor_guest as processor_guest
from datetime import timedelta


guest = Blueprint("guest",__name__, static_folder="static", template_folder="templates")


@guest.route("/home")
@guest.route("/")
def home():
    return render_template('guest/index.html')


@guest.route('/chatbot_guest', methods=["POST"])
def chatbot_guest():
    if request.method == 'POST':
        the_question = request.form['question']
        response = processor_guest.chatbot_response(the_question)
    return jsonify({"response": response })


@guest.route("/faq")
def faq():
    return render_template('guest/faq.html')


@guest.route('/logout')
def logout():
    session.pop('studentCode',None)
    session.permanent = False
    return redirect(url_for('home'))


@guest.errorhandler(400)
def handle_bad_request(e):
    return render_template('errors/client/400.html'), 400


@guest.errorhandler(403)
def handle_bad_request(e):
    return render_template('errors/client/400.html'), 403


@guest.errorhandler(404)
def not_found(self):
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