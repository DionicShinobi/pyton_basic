def common_elements():

    # Створюємо множини чисел кратних 3 та 5
    multiples_of_3 = set(range(0, 100, 3))
    multiples_of_5 = set(range(0, 100, 5))

    # Знаходимо перетин двох множин
    intersection = multiples_of_3 & multiples_of_5

    return intersection


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}


