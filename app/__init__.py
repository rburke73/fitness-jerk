from flask import Flask
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required

# Crea
__author__ = 'rburke'

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
# Fix this - pull it from config.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'


