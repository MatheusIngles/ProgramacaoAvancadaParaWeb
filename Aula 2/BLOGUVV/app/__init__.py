# app/__init__.py
# pip install flask flask-wtf flask-sqlalchemy flask-migrate datepipotime flask-login

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

from flask_login import LoginManager

app = Flask(__name__)
app. config.from_object(Config)
db= SQLAlchemy(app)
Migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view =  'login'
from app import routes, models 