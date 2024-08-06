import string

# Введення даних з якими в подальшому і будемо працювати
s = input("Enter the line: ")

# Видалення пунктуації
s = s.translate(str.maketrans('', '', string.punctuation))

# Перетворення першої літери кожного слова на велику та створення хештегу
hashtag = '#' + s.title().replace(' ', '')

# Скорочення до 140 символів, якщо потрібно
hashtag = hashtag[:140]

# Результат
print(hashtag)
