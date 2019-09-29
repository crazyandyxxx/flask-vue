from flask import Flask, jsonify, render_template, Blueprint, redirect, url_for, request, make_response
from flask_httpauth import HTTPBasicAuth
from flask_login import login_required, LoginManager
from flask_cors import CORS
import os
import logging
from random import randint
from models import User, db, migrate

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__,
                static_folder = "../dist/static",
                template_folder = "../dist")
    app.logger.setLevel(logging.INFO)
    app.logger.info('Server startup')
    CORS(app, supports_credentials=True)
    return app

app = create_app()
app.secret_key = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
auth = Blueprint('auth',__name__)
db.init_app(app)
migrate.init_app(app, db)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@auth.after_app_request
def after_request(resp):
	resp = make_response(resp)
	resp.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8080'
	resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
	resp.headers['Access-Control-Allow-Headers'] = 'content-type,token'
	return resp

# Http auth
httpAuth = HTTPBasicAuth()

@httpAuth.verify_password
def verify_password(username_token):
	username_token = request.headers.get('Token')
	if username_token == '':
		return False
	else:
		g.currnet_user = User.verify_auth_token(username_token)
		g.token_used = True
		return g.currnet_user is not None

@auth.route('/login', methods=['POST'])
def login():
    json = request.get_json()
    user = User.query.filter_by(username = json['username']).first()
    if user.verify_password(json['password']):
        g.currnet_user = user
        token = user.generate_auth_token(expiration=3600)
        return token
    return "Invalid username or password"

@auth.route('/register', methods=['POST'])
def register():
    json = request.get_json()
    user = User(username=json['username'])
    user.set_password(json['password'])
    db.session.add(user)
    db.session.commit()
    return 'Success'

@httpAuth.login_required
@app.route('/api/random', methods=['GET'])
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
