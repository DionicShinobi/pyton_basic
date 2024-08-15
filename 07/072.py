def correct_sentence(text):

    # Робимо першу букву великою
    text = text[0].upper() + text[1:]

    # Додаємо крапку в кінець, якщо її немає
    if not text.endswith('.'):
        text += '.'

    return text


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

print('ОК')
