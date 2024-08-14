def add_one(some_list):

    # Перетворення списку цифр у число
    number = int(''.join(map(str, some_list)))

    # Додавання 1
    number += 1

    # Перетворення числа назад у список цифр
    return list(map(int, str(number)))


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'

print("ОК")
