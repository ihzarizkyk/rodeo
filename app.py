# Rodeo App

from flask import (Flask, render_template, url_for, abort)

app = Flask(__name__)

@app.route("/")
def index:
	return "testing flask app"