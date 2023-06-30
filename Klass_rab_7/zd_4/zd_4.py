"""
Задание №4
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
"""
import os
import random
from random import randint, randbytes, sample
from string import ascii_letters


# def random_extension(list_ext: list[str]) -> str:
#     return random.choice(list_ext)
#
# def create_files(extension: list[str], dir: str, min_name: int = 6, max_name: int = 30,
#                  min_size=256, max_size: int = 4096, amount: int = 42):
#     for _ in range(amount):
#         name_size = randint(min_name, max_name)
#         ext = random_extension(extension)
#         file_name = ''.join(sample(ascii_letters, name_size)) + '.' + ext
#         if not os.path.exists(dir):
#             os.mkdir(dir)
#         full_name = os.path.join(dir, file_name)
#         if os.path.exists(full_name):
#             continue
#         with open(full_name, 'ab') as file:
#             size = randint(min_size, max_size)
#             result = randbytes(size)
#             file.write(result)
#
#
# create_files(['txt', 'doc', 'md', 'rtf', 'jpg', 'png', 'bmp', 'mp3', 'ogg', 'wav',
#               'mp4', 'avi', 'mov'], dir='test', amount=50)

def file_sorter(path: str):
    for folder in ['video', 'music', 'audio', 'docs']:
        if not os.path.exists(folder):
            os.mkdir(folder)

    for file in os.listdir(path):
        extension = file.split('.')[1]
        if extension in ['txt', 'doc', 'md']:
            os.replace(file, os.path.join(os.getcwd(), 'docs', file))

file_sorter('test')