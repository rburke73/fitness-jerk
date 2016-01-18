from flask.ext.sqlalchemy import SQLAlchemy
from .. import app

__author__ = 'rburke'

db = SQLAlchemy(app)

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))
