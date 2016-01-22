from app import db
from flask.ext.security import RoleMixin
from sqlalchemy import PrimaryKeyConstraint


class RolesUsers(db.Model, RoleMixin):
    __tablename__ = 'roles_users'
    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'role_id'),
    )
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id'))

