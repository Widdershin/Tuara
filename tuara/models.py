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

def register_for_admin(classes):
    for cls in classes:
        admin.register(cls, session=db.session)

register_for_admin([Organization, Skill])