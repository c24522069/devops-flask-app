from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return f'Greeting <a href="{url_for("contact")}">Contact</a>'

@app.route('/about')
def talk_about():
	return '<p>This app runs using the Flask web framework<p><br><a href="https://flask.palletsprojects.com/en/stable/">Check out the framework here</a><br><a href="https://python.org">Check out python here</a>'

@app.route('/contact')
def contact():
    return "Contact me at C24522069@mytudublin.ie"


