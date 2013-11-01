from flask import Flask, render_template, url_for, request
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
    return render_template('specific_skill.html', skill=skill)

@app.context_processor
def add_app_details():
    return {"app_name": APP_NAME, "app_description": APP_DESCRIPTION}

@app.context_processor
def generate_header_links():
    header_links = [("Organizations", organizations), ("Skills", skills)]

    processed_header_links = []

    #TODO: Handle url matching for suburls
    for label, func in header_links:
        url = url_for(func.__name__)
        active = request.path == url
        processed_header_links.append((label, url, active))


    return dict(header_links=processed_header_links)

if __name__ == '__main__':
    app.run(debug=True)