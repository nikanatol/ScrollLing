import json
from flask import render_template, request
from scrollling import app

def load_data():
    """Загружает данные из JSON-файла."""
    with open('scrollling/data/words.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    # Получаем язык из запроса, по умолчанию 'en'
    lang = request.args.get('lang', 'en')
    
    # Загружаем все данные
    all_words = load_data()
    
    # Готовим данные для конкретного языка
    # (Это упрощенная логика, можно оптимизировать)
    display_words = []
    for item in all_words:
        display_words.append({
            'word': item['translations'].get(lang, item['base_word']),
            'image': item['image']
        })

    # Передаем язык и список слов в шаблон
    return render_template('index.html', words=display_words, current_lang=lang)

