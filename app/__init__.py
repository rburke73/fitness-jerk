import urllib
import urlparse
from flask import Flask
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'

db = SQLAlchemy(app)

from models import User, Role

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


# Create a user to test with.
# TODO Remove this once registration and admin screens are added
@app.before_first_request
def create_user():
    db.create_all()
    user_datastore.create_user(email='jerk@foo.bar', password='password')
    db.session.commit()

# This is a fix for the Flask Security v2.6/2.7 problem of urlencode being missing as a filter.
# This code was pulled from a github comment: https://github.com/mitsuhiko/jinja2/issues/17
# TODO Review if this is the best way to do this.
@app.template_filter('urlencode')
def urlencode(uri, **query):
   parts = list(urlparse.urlparse(uri))
   q = urlparse.parse_qs(parts[4])
   q.update(query)
   parts[4] = urllib.urlencode(q)
   return urlparse.urlunparse(parts)
app.jinja_env.globals['urlencode'] = urlencode

import views
