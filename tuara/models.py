from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.mongoengine import Document
from __init__ import db, admin

class Organization(Document):
    name = db.StringField(required=True, max_length=30)
    description = db.StringField(required=True, max_length=400)
    email = db.StringField(required=True, max_length=200)
    skills = db.ListField(db.ReferenceField('Skill'))

    def __str__(self):
        return self.name

class Skill(Document):
    name = db.StringField(max_length=30, required=True)
    description = db.StringField(max_length=200, required=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class User(Document):
    email = db.StringField(max_length=200, required=True)
    user_name = db.StringField(max_length=20, required=True)
    password_hash = db.StringField(max_length=67)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_authenticated():
        pass

    def __repr__(self):
        pass
    #    return self.email, self.user_name


def register_for_admin(classes):
    for cls in classes:
        admin.register(cls)

register_for_admin([Organization, Skill, User])