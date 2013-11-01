from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db, admin

skills = db.Table('skills',
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id')),
    db.Column('organization_id', db.Integer, db.ForeignKey('organization.id'))
)

class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(400), default="")
    email = db.Column(db.String(60))
    skills = db.relationship('Skill', secondary=skills,
        backref=db.backref('organizations', lazy='dynamic'))

    def __init__(self, name=name, description=description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(200), default="")

    def __repr__(self):
        return self.name

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200))
    user_name = db.Column(db.String(20))
    password_hash = db.Column(db.String(67))

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
        admin.register(cls, session=db.session)

register_for_admin([Organization, Skill, User])