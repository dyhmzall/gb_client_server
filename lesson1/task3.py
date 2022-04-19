"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.
"""


def check_str_to_bytes(word):
    try:
        word.encode('ascii')
    except UnicodeEncodeError as e:
        return False

    return True


words = ['attribute', 'класс', 'функция', 'type']

for word in words:
    if check_str_to_bytes(word):
        print(f'"{word}" is possible to convert to bytes')
    else:
        print(f'"{word}" is NOT possible to convert to bytes')
