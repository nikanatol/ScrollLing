import json
from flask import render_template, request
from scrollling import app

def load_words():
    """Загружает слова из JSON-файла."""
    # Используйте with для автоматического закрытия файла
    with open('scrollling/data/words.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    # Получаем язык из URL (?lang=ru), по умолчанию 'en'
    lang = request.args.get('lang', 'en')
    
    words_data = load_words()
    
    # Подготовим данные для отображения
    display_data = []
    for item in words_data:
        display_data.append({
            # Выбираем перевод для нужного языка, если его нет - берем базовое слово
            'text': item['translations'].get(lang, item['base_word']),
            'image_url': item['image'],
            'pos': item['part_of_speech'] # pos - part of speech (часть речи)
        })

    # Передаем в шаблон список словарей и текущий язык
    return render_template('index.html', sentence=display_data, current_lang=lang)

