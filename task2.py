"""
GoIt Python Core 2.0

Homework Module 3

Завдання 2: генерує набір унікальних випадкових чисел у межах заданих параметрів  
"""
import random



def get_numbers_ticket(min_number: int, max_number: int, quantity: int) -> list:
    """
    Генерує унікальний відсортований список випадкових чисел у діапазоні [min_number, max_number].

    Args:
        min_number (int): мінімальне число (не менше 1)
        max_number (int): максимальне число (не більше 1000)
        quantity (int): кількість чисел, що потрібно отримати (менша за діапазон)

    Returns:
        list: відсортований список унікальних випадкових чисел
        None: якщо аргументи не відповідають умовам або мають неправильний тип
    """
    # Перевіряємо правильність аргументів
    if not isinstance(min_number, int) \
        or not isinstance(max_number, int) \
        or not isinstance(quantity, int):
        print("Attributes must be integers.")
        return None

    if min_number < 1 or max_number > 1000:
        print("Numbers must be in the range from 1 to 1000.")
        return None

    if max_number <= min_number or quantity > (max_number - min_number + 1):
        print("Invalid range or quantity.")
        return None

    numbers_set = set()
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min_number, max_number))
    number_list = list(numbers_set)
    return sorted(number_list)

ticket = get_numbers_ticket(1, 100, 10)
print("Ваші лотерейні числа:", ticket)
