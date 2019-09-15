from app import app
import models
import views

#Создаем точку входа __name__ == '__main__':
if __name__ == '__main__':
    app.run(debug=True)
