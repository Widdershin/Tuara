from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.superadmin import Admin, model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://testacc:testpass@localhost/testdb'
db = SQLAlchemy(app)
admin = Admin(app)
app.config.from_object('config')

import models