from flask import Flask, redirect, render_template, request, url_for
from apps.ingc.ingc import ingc
from apps.guest.guest import guest
from config import configs
from apps.utils.database import *
from flask_mail import Mail, Message
import os
#from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.register_blueprint(ingc, url_prefix="/ingc")
app.register_blueprint(guest, url_prefix="/guest")
app.config.from_object(configs[os.environ.get("FLASK_ENV", "development")])
mysql.init_app(app)
mail = Mail(app)
#csrf = CSRFProtect()
#csrf.init_app(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/section")
def section():
    return render_template('section.html')


@app.errorhandler(400)
def handle_bad_request(e):
    return render_template('errors/client/400.html'), 400


@app.errorhandler(403)
def handle_bad_request(e):
    return render_template('errors/client/400.html'), 403


@app.errorhandler(404)
def not_found(self):
    return render_template('errors/client/404.html'), 404


@app.errorhandler(405)
def method_not_found(error):
    return render_template('errors/client/405.html'), 405


@app.errorhandler(408)
def request_timeout(error):
    return render_template('errors/client/408.html'), 408


@app.errorhandler(410)
def page_gone(error):
    return render_template('errors/client/410.html'), 410


@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/server/500.html'), 500

@app.errorhandler(505)
def http_not_compatible(error):
    return render_template('errors/server/500.html'), 505


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
