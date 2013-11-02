from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.mongoengine import Document, ValidationError
from slugify import slugify
from __init__ import db, admin

class Organization(Document):
    name = db.StringField(required=True, max_length=30)
    description = db.StringField(required=True, max_length=400)
    email = db.StringField(required=True, max_length=200)
    skills = db.ListField(db.ReferenceField('Skill'))

    def __str__(self):
        return self.name

class Skill(Document):
    name = db.StringField(max_length=30, required=True, unique=True)
    description = db.StringField(max_length=200, required=True)
    slug = db.StringField(required=True, max_length=30)

    def clean(self):
        self.slug = slugify(self.name)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class User(Document):
    email = db.StringField(max_length=200, required=True, unique=True)
    user_name = db.StringField(max_length=20, required=True, unique=True)
    password_hash = db.StringField(max_length=67)

    def clean(self):
        if not self.password_hash:
            raise ValidationError("You must set the user's password with set_password before saving")

    def set_password(self, password):

        password_len = len(password)
        
        if not 8 < password_len < 256:
            raise ValidationError("Passwords must be greater than 8 chars and less than 256 chars")

        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_authenticated():
        pass

    def __repr__(self):
        return self.user_name
    #    return self.email, self.user_name


def register_for_admin(classes):
    for cls in classes:
        admin.register(cls)

register_for_admin([Organization, Skill, User])