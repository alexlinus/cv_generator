from app import manager
#Создаем для управления приложениями типа migrate, init, commit
from main import *
import views

#запускаем manager
if __name__ == '__main__':
    manager.run()