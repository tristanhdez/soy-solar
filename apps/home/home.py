from flask import Blueprint, render_template


home = Blueprint("home",__name__, static_folder="static", template_folder="templates")


@home.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["HTTP-HEADER"] = "VALUE"
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    #response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response


@home.route("/")
def index():
    return render_template('home/index.html')


@home.route("/section")
def section():
    return render_template('home/section.html')


@home.errorhandler(400)
def handle_bad_request(e):
    return render_template('errors/client/400.html'), 400


@home.errorhandler(403)
def handle_bad_request(e):
    return render_template('errors/client/400.html'), 403


@home.errorhandler(404)
def not_found(self):
    return render_template('errors/client/404.html'), 404


@home.errorhandler(405)
def method_not_found(error):
    return render_template('errors/client/405.html'), 405


@home.errorhandler(408)
def request_timeout(error):
    return render_template('errors/client/408.html'), 408


@home.errorhandler(410)
def page_gone(error):
    return render_template('errors/client/410.html'), 410


@home.errorhandler(500)
def internal_error(error):
    return render_template('errors/server/500.html'), 500


@home.errorhandler(505)
def http_not_compatible(error):
    return render_template('errors/server/500.html'), 505
