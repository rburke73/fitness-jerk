from app import app
from flask import render_template


@app.route('/goal')
def goal_list():
    return render_template('goal.html')

