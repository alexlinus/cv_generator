from app import app
from flask import render_template
from forms import CvForm, EducationForm

@app.route('/')
def index():
    cv_form = CvForm()
    education_form = EducationForm()
    return render_template('index.html', cv_form=cv_form, education_form=education_form)