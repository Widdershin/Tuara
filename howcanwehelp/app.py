from flask import Flask, render_template
from __init__ import app, db
import models

@app.route('/')
def test():
    orgs = models.Organization.query.all()

    #return "".join(["<p>{}: {}</p>\n".format(org.name, org.description) for org in orgs])
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)