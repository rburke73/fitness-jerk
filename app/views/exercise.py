from app import app
from flask import render_template


@app.route('/exercise')
def exercise_list():
    return render_template('exercise.html')

