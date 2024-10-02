"""
GoIt Python Core 2.0

Homework Module 3

Завдання 3: нормалізує телефонні номери до стандартного формату 
"""
import re



def normalize_phone(phone_number: str) -> str:
    """
    Нормалізує номер телефону, прибираючи всі символи, окрім цифр та '+',
    а також виправляє префікс до +38, якщо він відсутній.

    Args:
        phone_number (str): Вхідний номер телефону в будь-якому форматі.

    Returns:
        str: Нормалізований номер телефону у форматі +38XXXXXXXXXX.
    """
    # Видаляємо всі символи, окрім цифр і '+'
    normalized_phone = re.sub(r"[^\d\+]", "", phone_number)

    # Додаємо префікс '+38', якщо його немає
    normalized_phone = re.sub(r"^(?!\+)(38)", r"+\1", normalized_phone)
    normalized_phone = re.sub(r"^(?!\+38)", r"+38", normalized_phone)

    return normalized_phone


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
