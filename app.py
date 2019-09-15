from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)

app.config.from_object(Configuration)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
#регистрируем комманду, которую мы будем использовать в консоли для миграций
manager.add_command('db', MigrateCommand)

from models import CV, Education

admin = Admin(app, 'FlaskApp', url='/', index_view=AdminIndexView(name='Home'))
admin.add_view(ModelView(CV, db.session))
admin.add_view(ModelView(Education, db.session))


#@app.route('/')
#def hello_world():
 #   return 'Hello World!'


if __name__ == '__main__':
    app.run()
