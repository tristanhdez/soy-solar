from flask import Flask, render_template
from apps.ingc.ingc import ingc
from apps.guest.guest import guest


app = Flask(__name__)
app.register_blueprint(ingc, url_prefix="/ingc")
app.register_blueprint(guest, url_prefix="/guest")


@app.route("/")
def home():
    return "<h1>MAIN PAGE</h1>"


if __name__ == "__main__":
    app.run(debug=True)
