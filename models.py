import datetime
from app import app, db

class CV(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(55), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(65), nullable=True)
    city = db.Column(db.String(40), nullable=False)
    citizenship = db.Column(db.String, nullable=True)
    about = db.Column(db.Text, nullable=True)
    skills = db.Column(db.String(200), nullable=True)
    languages = db.Column(db.String(100), nullable=True)
    position = db.Column(db.String(100), nullable=True)
    #https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.choice, но нужно переопредялять db на sqlaclhemy_utils вместо SQLACLCHEMY в app.py
    work_schedule = db.Column(db.String(100), default='Полный рабочий день')
