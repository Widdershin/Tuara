from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.superadmin import Admin, model
from flask.ext.login import LoginManager, login_user, login_required
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://testacc:testpass@localhost/testdb'

db = SQLAlchemy(app)

admin = Admin(app)

login_manager = LoginManager()
login_manager.init_app(app)

sys.path.append('..\\')
app.config.from_object('tuara.config')

metadata = db.MetaData(bind=db.engine)

import models