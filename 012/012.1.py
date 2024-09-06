import codecs
import re


def extract_html_content(html_file, result_file='cleaned.txt'):
    # Открываем HTML-файл с кодировкой UTF-8
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html_content = file.read()

    # Регулярное выражение для поиска HTML-тегов и их содержимого
    html_tags = re.findall(r'<[^>]+>', html_content)

    # Записываем HTML-теги и их содержимое в новый файл
    with codecs.open(result_file, 'w', 'utf-8') as output_file:
        for tag in html_tags:
            output_file.write(tag + "\n")

    print(f"HTML теги сохранены в файл {result_file}")


# Пример вызова функции
extract_html_content('draft.html', 'clean.txt')
