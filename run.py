from scrollling import app

if __name__ == "__main__":
    # Этот блок используется для запуска в режиме отладки, например: python run.py
    # Для продакшена используется uWSGI, который импортирует 'app' отсюда.
    app.run(host='0.0.0.0', port=1234, debug=True)

