from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    fruits = ['Banana', 'Oranges', 'Apples']
    return render_template('index.html', fruits=fruits)


@app.route('/Developer/<int:dev_id>')
def developer(dev_id):
    lang = "python"
    framework = "Flask"
    return "My id is <b>{}</b> and i code using {} and i also use {}".format(dev_id, lang, framework)


@app.route('/about/<name>')
def greetings(name):
    name_length = len(name)
    return render_template('greetings.html', the_name=name, name_length=len(name))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact_us')
def contacts():
    return render_template('contact_us.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500'), 500


if __name__ == '__main__':
    app.run(debug=True, port=8080)
