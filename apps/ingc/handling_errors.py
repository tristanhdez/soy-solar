from flask import render_template
from apps.ingc.ingc import ingc

@ingc.errorhandler(400)
def handle_bad_request(e):
    return render_template('errors/400.html'), 400


@ingc.errorhandler(403)
def handle_bad_request(e):
    return render_template('errors/400.html'), 403


@ingc.errorhandler(404)
def not_found(self):
    return render_template('errors/404.html'), 404


@ingc.errorhandler(405)
def method_not_found(error):
    return render_template('errors/405.html'), 405


@ingc.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500
