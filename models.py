import datetime
from app import app, db


cv_education = db.Table('cv_education',
    db.Column('cv_id', db.Integer, db.ForeignKey('CV.id')),
    db.Column('education_id', db.Integer, db.ForeignKey('education.id'))
    )

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
    education = db.relationship('Education', secondary=cv_education, backref=db.backref('cv', lazy='dynamic'), cascade="all, delete-orphan", single_parent=True)

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    study_place = db.Column(db.String(200), nullable=False)
    specialty_faculty = db.Column(db.String(200), nullable=True)
    start_study = db.Column(db.Date(), nullable=True)
    end_study = db.Column(db.Date(), nullable=True)