from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bootstrap import Bootstrap



class config:

    SECRET_KEY = 'secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123456789@localhost/apiscrapy'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    JWT_SECRET_KEY = 'my-secret-key'

    PORT = "5000"
    HOST = "localhost"


class TestingConfig(config):

    DEBUG = True
    TESTING = True
    PORT = "8080"
    HOST = "0.0.0.0"



class AppFlask:

    app = Flask(__name__)
    app.config.from_object(TestingConfig)

    api = Api(app)
    db = SQLAlchemy(app)
    loginManager = LoginManager(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)
    bootstrap = Bootstrap(app)




