from flask import Blueprint, render_template, jsonify, request
import apps.ingc.processor_ingc as processor_ingc

ingc = Blueprint("ingc",__name__, static_folder="static", template_folder="templates")


@ingc.route("/home")
@ingc.route("/")
def home():
    return render_template('ingc/index.html')

@ingc.route('/chatbot_ingc', methods=["GET", "POST"])
def chatbotResponse():
    if request.method == 'POST':
        the_question = request.form['question']
        response = processor_ingc.chatbot_response(the_question)
    return jsonify({"response": response })