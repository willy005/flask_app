from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome home!'


@app.route('/about')
def about():
    return 'Welcome to about page'


@app.route('/contact_us')
def contacts():
    return 'Get in touch with us'


@app.errorhandler(404)
def page_not_found(e):
    return 'Page not found', 404


@app.errorhandler(500)
def internal_server_error(e):
    return 'Internal Server Error', 500


if __name__ == '__main__':
    app.run(debug=True, port=8080)
