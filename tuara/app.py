from flask import Flask, render_template, url_for
from __init__ import app, db, models

APP_NAME = "Tuara"
APP_DESCRIPTION = """
{} is a platform aimed at connecting people with niche
 skills with the organizations in their community that their help could most impact.
 """.format(APP_NAME)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/organizations/')
def organizations():
    orgs = models.Organization.query.all()
    return render_template('organizations.html', orgs=orgs)

@app.route('/skills/')
def skills():
    skills = models.Skill.query.all()
    return render_template('skills.html', skills=skills)

@app.route('/skills/<int:skill_id>/')
def specific_skill(skill_id):
    skill = models.Skill.query.get_or_404(skill_id)
    return skill.name

@app.context_processor
def add_app_details():
    return {"app_name": APP_NAME, "app_description": APP_DESCRIPTION}

@app.context_processor
def generate_header_links():
    header_links = [("Main", main), ("Organizations", organizations), ("Skills", skills)]
    return dict(header_links=[(label, url_for(str(func.__name__))) for label, func in header_links])

if __name__ == '__main__':
    app.run(debug=True)