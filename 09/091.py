def popular_words(text, words):
    # Приведення тексту до нижнього регістру та розбиття на окремі слова
    text_words = text.lower().split()

    # Словник для збереження результатів
    word_count = {}

    # Рахуємо кількість появ кожного слова зі списку у тексті
    for word in words:
        word_count[word] = text_words.count(word)

    return word_count


assert popular_words('''When I was One I had just begun When I was Two I was nearly new''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'

print('OK')