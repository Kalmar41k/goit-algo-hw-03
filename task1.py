"""
GoIt Python Core 2.0

Homework Module 3

Завдання 1: розрахує кількість днів між заданою датою і поточною датою 
"""
from datetime import datetime



def get_days_from_today(date: str) -> int:
    """
    Обчислює кількість днів між сьогоднішньою датою та переданою датою у форматі 'YYYY-MM-DD'.

    Args:
        date (str): Дата у форматі 'YYYY-MM-DD'.

    Returns:
        int: Кількість днів між сьогоднішньою датою та вказаною датою.
        None: Якщо передано неправильний формат дати.
    """
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        result = abs((today - date).days)
        return result
    except ValueError:
        print("Unknown date format. Try this format: 'YYYY-MM-DD'")
        return None

difference = get_days_from_today("2024-10-01")
print(f"Різниця між датами {difference} днів.")
