from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

class config:

    SECRET_KEY = 'secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123456789@localhost/apiscrapy'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class AppFlask:

    app = Flask(__name__)
    app.config.from_object(config)
    app.config["DEBUG"] = True
    app.config['JWT_SECRET_KEY'] = 'my-secret-key'

    api = Api(app)
    db = SQLAlchemy(app)
    login_manager = LoginManager(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)




