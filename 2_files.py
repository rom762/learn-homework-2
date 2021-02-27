"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""


def main():
    filename = 'referat.txt'
    with open(filename, 'r', encoding='UTF-8') as f:
        data = f.read()

    print(f'1. Symbols: {len(data)}')
    print(f'3. Words: {len(data.split())}')
    data = data.replace('.', '!')

    with open('referat2.txt', 'w', encoding='UTF-8') as ff:
        ff.write(data)


def check_it():
    with open('referat2.txt', 'r', encoding='UTF-8') as ff:
        lines = ff.readlines()
        print(*lines, sep='\n')


if __name__ == "__main__":
    main()
    check_it()
