from flask import Blueprint, render_template, request, jsonify
import apps.guest.processor_guest as processor_guest

guest = Blueprint("guest",__name__, static_folder="static", template_folder="templates")


@guest.route("/home")
@guest.route("/")
def home():
    return render_template('guest/index.html')


@guest.route('/chatbot_guest', methods=["GET", "POST"])
def chatbotResponse():
    if request.method == 'POST':
        the_question = request.form['question']
        response = processor_guest.chatbot_response(the_question)
    return jsonify({"response": response })