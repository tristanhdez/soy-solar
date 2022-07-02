from flask import Flask
from apps.ingc.ingc import ingc
from apps.guest.guest import guest
from config import configs
import os
#from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.register_blueprint(ingc, url_prefix="/ingc")
app.register_blueprint(guest, url_prefix="/guest")
app.config.from_object(configs[os.environ.get("FLASK_ENV", "development")])
#csrf = CSRFProtect()
#csrf.init_app(app)


@app.route("/")
def home():
    return "<h1>MAIN PAGE</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
