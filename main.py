from flask import Flask, render_template
from apps.ingc.ingc import ingc
from apps.guest.guest import guest
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
app.register_blueprint(ingc, url_prefix="/ingc")
app.register_blueprint(guest, url_prefix="/guest")
app.config['SECRET_KEY'] = 'SECRET_KEY_:)'
#app.config.update(
#    SESSION_COOKIE_SECURE=True,
#    SESSION_COOKIE_HTTPONLY=True,
#    SESSION_COOKIE_SAMESITE='Lax',
#)
#response.set_cookie('username', 'flask', secure=True, httponly=True, samesite='Lax')
#csrf = CSRFProtect()
#csrf.init_app(app)


@app.route("/")
def home():
    return "<h1>MAIN PAGE</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
