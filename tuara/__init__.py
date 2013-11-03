from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.superadmin import Admin, model
from flask.ext.login import LoginManager
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://testacc:testpass@localhost/testdb'

sys.path.append('..\\')
app.config.from_object('tuara.config')

db = MongoEngine(app)

admin = Admin(app)

login_manager = LoginManager()
login_manager.init_app(app)

import models