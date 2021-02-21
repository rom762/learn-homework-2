"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta
import locale

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = datetime.today()
    print(f'Вчера: {today - timedelta(days=1)}')
    print(f'Сегодня: {today}')
    print(f'Завтра: {today + timedelta(days=1)}')
    print(f'30 дней назад: {today - timedelta(days=30)}')


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    str_format = '%d/%m/%y %H:%M:%S.%f'
    return datetime.strptime(date_string, str_format)


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))

