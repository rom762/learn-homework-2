"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

users = [
    {'name': 'John', 'age': 45, 'job': 'driver'},
    {'name': 'Jack', 'age': 19, 'job': 'soldier'},
    {'name': 'Linda', 'age': 54, 'job': 'writer'},
    {'name': 'Eva', 'age': 23, 'job': 'student'},
]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    columns = list(users[0].keys())
    with open('users.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, columns, delimiter=';')
        writer.writeheader()
        for user in users:
            writer.writerow(user)


if __name__ == "__main__":
    main()
