from .. import app
from flask import render_template
from flask.ext.security import login_required

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html')

