from ..app import db


class User(db.Model):
    user_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    user_mail = db.Column(db.Text, nullable=False)
    user_pseudo = db.Column(db.String(30), nullable=False)
    user_name = db.Column(db.Text, nullable=False)
    user_password = db.Column(db.String(64), nullable=False)
