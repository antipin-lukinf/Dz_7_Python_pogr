"""
Задание №1
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""
import random

my_text = list()

strings_count = 0


def read_file(strings_count=3, file_name='text_data.txt'):
    strings_count_1 = strings_count
    with open(file_name, 'a+', encoding='utf-8') as f:
        for i in range(strings_count_1):
            text_int = str(random.randint(-1000, 1000))
            text_float = str(round(random.uniform(-1000, 1000), 3))
            my_text.append(text_int)
            my_text.append(text_float)
            my_text.append('\n')
        f.write('|'.join(my_text))


        f.close()


read_file(3)
