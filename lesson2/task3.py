"""
3. Задание на закрепление знаний по модулю yaml.
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке
ASCII (например, €);

Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла
с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""

import yaml

SOURCE_DICT = {
    'key1': ['value1', 'value2', 'value3'],
    'key2': 500,
    'key3': {
        'key4': '€',
        'key5': '₴',
        'key6': '₽'
    }
}

with open('task3/file.yaml', 'wt', encoding='utf-8') as f:
    yaml.dump(SOURCE_DICT, f, default_flow_style=False, allow_unicode=True)

with open('task3/file.yaml', 'rt', encoding='utf-8') as f:
    result_dict = yaml.load(f, Loader=yaml.FullLoader)

print(SOURCE_DICT == result_dict)
