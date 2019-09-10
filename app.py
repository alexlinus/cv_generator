from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.config.from_object(Configuration)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
#регистрируем комманду, которую мы будем использовать в консоли для миграций
manager.add_command('db', MigrateCommand)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
