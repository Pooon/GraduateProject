from flask import Flask
from GraduateProject.config.config import Config
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager

app = Flask(__name__)

app.config.from_object(Config)
Config.init_app(app)
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)

login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'

import api
