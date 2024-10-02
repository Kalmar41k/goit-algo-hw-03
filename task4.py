"""
GoIt Python Core 2.0

Homework Module 3

Завдання 4: виводить список колег, яких потрібно привітати з днем народження на один тиждень вперед.
"""
from datetime import datetime, date, timedelta



def string_to_date(date_string: str) -> date:
    """
    Перетворює рядковий тип дати на об'єкт datatime.date().

    Args:
        date_string (str): Вхідний рядок дати у форматі "YYYY.MM.DD".

    Returns:
        date: Об'єкт datatime.date() у форматі "YYYY-MM-DD".
    """
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(formatted_date: date) -> str:
    """
    Перетворює об'єкт datatime.date() на рядок.

    Args:
        formatted_date (str): Вхідний рядок дати у форматі "YYYY.MM.DD".

    Returns:
        str: рядок у форматі "YYYY.MM.DD".
    """
    return formatted_date.strftime("%Y.%m.%d")


def prepare_user_list(user_data: list) -> list:
    """
    Перетворює список з даними користувачів на список, де значення в словнику з 
    ключем "birthday" - стає об'єктом замість рядка.

    Args:
        user_data (list): Вхідний список зі словників про дані користувача, у яких ключ-значення:
        "name": str, "birthday": str.

    Returns:
        list: Список зі словників про дані користувача, у яких ключ-значення:
        "name": str, "birthday": date.
    """
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def find_next_weekday(start_date: date, weekday: int) -> date:
    """
    Знаходить наступний вказаний день тижня, враховуючи дату початку.

    Args:
        start_date (date): Дата, з якої починається пошук.
        weekday (int): Цільовий день тижня (0 - понеділок, 6 - неділя).

    Returns:
        date: Дата наступного цільового дня тижня.
    """
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday: date) -> date:
    """
    Коригує дату народження, якщо вона припадає на вихідні дні (субота або неділя).

    Args:
        birthday (date): Дата народження.

    Returns:
        date: Коригована дата (якщо потрібно) або оригінальна дата.
    """
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday


def get_upcoming_birthdays(users: list, days: int=7) -> list:
    """
    Збирає список найближчих днів народження користувачів у межах вказаних днів.

    Args:
        users (list): Список зі словників про користувачів, 
                      у яких ключ-значення:
                      "name": str, "birthday": str.
        days (int): Кількість днів, протягом яких потрібно шукати дні народження.

    Returns:
        list: Список словників, де кожен словник містить 
              "name" та "congratulation_date".
    """
    users = prepare_user_list(users)
    upcoming_birthdays = []
    today = date.today()

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = user["birthday"].replace(year=today.year + 1)

        if 0 <= (birthday_this_year - today).days <= days:

            birthday_this_year = adjust_for_weekend(birthday_this_year)

            congratulation_date_str = date_to_string(birthday_this_year)
            upcoming_birthdays.append({"name": user["name"],
                                        "congratulation_date": congratulation_date_str})
    return upcoming_birthdays


birthdays = [
    {"name": "Bill Gates", "birthday": "1955.10.03"},
    {"name": "Steve Jobs", "birthday": "1955.10.05"},
    {"name": "Jinny Lee", "birthday": "1956.10.07"},
    {"name": "Sarah Lee", "birthday": "1957.10.09"},
    {"name": "Jonny Lee", "birthday": "1958.10.11"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming = get_upcoming_birthdays(birthdays)
print("Потрібно привітати у найближчі дні: ", upcoming)
