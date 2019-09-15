from wtforms import Form, StringField, TextAreaField
from models import CV, Education
from wtforms_alchemy import ModelForm, ModelFieldList
from wtforms.fields import FormField, FieldList
from wtforms.fields.html5 import DateField

class EducationForm(ModelForm):
    class Meta:
        model = Education
        field_args = {
                    'study_place': {'label': 'Учебное заведение'},
                    'specialty_faculty': {'label': 'Факультет\Специальность'},
                    'start_study': {'label': 'Начало обучения', 'format': '%Y-%m'},
                    'end_study': {'label': 'Окончание обучения', 'format': '%Y-%m'},
                      }

class CvForm(ModelForm):
    class Meta:
        model = CV
        field_args = {'fio': {'label': 'ФИО'},
                      'date_of_birth': {'label': 'Дата рождения'},
                      'phone': {'label': 'Телефон'},
                      'email': {'label': 'E-mail'},
                      'city': {'label': 'Город проживания'},
                      'citizenship': {'label': 'Гражданство'},
                      'about': {'label': 'О себе'},
                      'skills': {'label': 'Навыки'},
                      'languages': {'label': 'Языки'},
                      'position': {'label': 'Желаемая должность'},
                      'work_schedule': {'label': 'График'},
                      'education': {'label': 'Образование'},
                      }

    cv_education = FieldList(FormField(EducationForm, label='Образование'), min_entries=2)
