from flask import Flask

# Создаем экземпляр приложения
app = Flask(__name__)

# Импортируем обработчики URL (views) после создания app,
# чтобы избежать циклических импортов.
from scrollling import views

