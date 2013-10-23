from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.superadmin import Admin, model
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://testacc:testpass@localhost/testdb'
db = SQLAlchemy(app)
admin = Admin(app)
sys.path.append('..\\')
app.config.from_object('tuara.config')
metadata = db.MetaData(bind=db.engine)

import models