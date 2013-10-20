from flask import Flask, render_template, url_for
from __init__ import app, db
import models

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/organizations/')
def organizations():
    orgs = models.Organization.query.all()
    return render_template('organizations.html', orgs=orgs)

@app.route('/skills/<int:skill_id>/')
def specific_skill(skill_id):
    skill = models.Skill.query.get_or_404(skill_id)
    return skill.name

@app.context_processor
def generate_header_links():
    header_links = [("Main", main), ("Organizations", organizations)]
    return dict(header_links=[(label, url_for(str(func.__name__))) for label, func in header_links])

if __name__ == '__main__':
    app.run(debug=True)