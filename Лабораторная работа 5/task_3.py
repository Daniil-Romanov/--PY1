from random import randint


def get_unique_list_numbers() -> list[int]:
    list_numbers = []
    while len(list_numbers) < 15:  # пока список не наполнится 15-ю элементами, будет выполняться.
        number = randint(-10, 10)  # генерация числа.
        if list_numbers.count(number) == 0:  # если числа нет в списке, то добавляется в список.
            list_numbers += [number]         # если нет, то на следующей итерации цикла сгенерируется новое число.
    return list_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
