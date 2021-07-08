import os
from flask import Flask, jsonify, g
from flask_cors import CORS

import models
from resources.shows import show

DEBUG = True
PORT = 5000

print(__name__)
app = Flask(__name__)

@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/')
def index():
    return 'hi'

CORS(show, origins=['http://localhost:3000', 'http://localhost:3000/popularapp', 'https://enigmatic-bayou-89258.herokuapp.com/', 'https://enigmatic-bayou-89258.herokuapp.com','https://enigmatic-bayou-89258.herokuapp.com/popularapp', 'https://enigmatic-bayou-89258.herokuapp.com/popularapp/'], supports_credentials=True)
app.register_blueprint(show, url_prefix='/api/v1/shows')

if 'ON_HEROKU' in os.environ: 
  print('\non heroku!')
  models.initialize()

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)