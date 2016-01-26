from app import app
from flask import render_template


@app.route('/food')
def food_list():
    return render_template('food.html')

