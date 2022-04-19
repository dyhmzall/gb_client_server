"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Далее забыть о том, что мы сами только что создали этот файл и исходить из того, что перед нами файл в неизвестной
кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан.
"""

import chardet

FILE_NAME = 'test_file.txt'


def create_file(filename, lines):
    with open(filename, 'tw', encoding='utf-8') as f:
        for line in lines:
            f.write(f'{line}\n')


lines = ['сетевое программирование', 'сокет', 'декоратор']

create_file(FILE_NAME, lines)

with open(FILE_NAME, 'br') as f:
    result = chardet.detect(f.read())
    f.seek(0)
    content = f.read().decode(result['encoding']).encode('utf-8')
    print(content.decode('utf-8'))
