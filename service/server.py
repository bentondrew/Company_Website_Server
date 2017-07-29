#  Copyright 2017
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED

from flask import (Flask,
                   render_template,
                   url_for)
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(32)

@app.route('/', methods=['GET'])
def home():
  return render_template('home.html')

@app.route('/services', methods=['GET'])
def services():
  return render_template('services.html')

@app.route('/about', methods=['GET'])
def about():
  return render_template('about.html')
