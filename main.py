from flask import Flask
from apps.student.student import student
from apps.guest.guest import guest
from apps.home.home import home
from config import configs
from apps.utils.database import *
import os


app = Flask(__name__, instance_relative_config=True)


app.register_blueprint(student, url_prefix="/student")
app.register_blueprint(guest, url_prefix="/guest")
app.register_blueprint(home, url_prefix="/")


app.config.from_object(configs[os.environ.get("FLASK_DEBUG", "development")])
app.config.from_pyfile('config.py', silent=True)


mysql.init_app(app)



if __name__ == "__main__":
    try:
        app.run(host='localhost', port=5000, debug=True)
    except Exception as e:
        print(str(e))
