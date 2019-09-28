from flask import Flask, jsonify, render_template, Blueprint, redirect, url_for
from flask_login import login_required, LoginManager
from flask_cors import CORS
import os
import logging
from random import randint

def create_app():
    app = Flask(__name__,
                static_folder = "../dist/static",
                template_folder = "../dist")
    app.logger.setLevel(logging.INFO)
    app.logger.info('Server startup')
    CORS(app)
    return app

app = create_app()
app.secret_key = 'you-will-never-guess'
auth = Blueprint('auth',__name__)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@auth.route('/login', methods=['GET','POST'])
def login():
    return redirect('/login')

@app.route('/api/random', methods=['GET'])
@login_required
def random_number():
    response = {
    'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

app.register_blueprint(auth, url_prefix='/auth')
