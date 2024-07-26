lists = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    [1],
    []
]

# Обробка кожного списку
for lst in lists:
    # Обчислити середину списку
    mid = (len(lst) + 1) // 2

    # Розділити список на два підсписки
    first_half = lst[:mid]
    second_half = lst[mid:]

    print(lst, "=>", [first_half, second_half])
