lists = [
    [12, 3, 4, 10],
    [1],
    [],
    [12, 3, 4, 10, 8]
]

# Обробка кожного списку і виведення початкового та зміненого списку
for lst in lists:
    if len(lst) > 1:
        modified_list = [lst[-1]] + lst[:-1]
    else:
        modified_list = lst
    # Виведення результату
    print(lst, '=>', modified_list)
