from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, url_for, request, redirect
from __init__ import app, db, models, login_manager, login_user, login_required

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
    orgs = models.Organization.objects
    return render_template('organizations.html', orgs=orgs)

@app.route('/skills/')
def skills():
    skills = models.Skill.objects
    return render_template('skills.html', skills=skills)

@app.route('/skills/<int:skill_id>/')
def specific_skill(skill_id):
    skill = models.Skill.query.get_or_404(skill_id)
    return render_template('specific_skill.html', skill=skill)

@app.route('/login/')
def login_page():
    return render_template('login.html')

@app.route('/post/login/', methods=['POST'])
def login():
    user = models.User.query.filter_by(email=request.values['email']).first_or_404()

    successful_login = user.check_password(request.values['password'])

    if successful_login:
        login_user(user)
        return redirect(url_for(main))

    return render_template('main.html')

@login_manager.user_loader
def load_user(id):
    return models.User.query.get(int(id))

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