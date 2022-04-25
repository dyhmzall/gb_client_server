"""
1. Задание на закрепление знаний по модулю CSV.
Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt
и формирующий новый «отчетный» файл в формате CSV. Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data
— и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
«Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;

Проверить работу программы через вызов функции write_to_csv().
"""

import re

import chardet
import csv


def get_data_from_contend(param, content):
    param_search = re.search(rf'{param}:\s*(.*)\r', content)
    return param_search[1]


def get_content_utf(content):
    return content.decode(chardet.detect(content)['encoding']).encode('utf-8').decode('utf-8')


def get_data(file_list):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for file in file_list:
        with open(file, 'rb') as f:
            content = get_content_utf(f.read())

            os_prod_list.append(get_data_from_contend('Изготовитель ОС', content))
            os_name_list.append(get_data_from_contend('Название ОС', content))
            os_code_list.append(get_data_from_contend('Код продукта', content))
            os_type_list.append(get_data_from_contend('Тип системы', content))

    main_data = [
        'Изготовитель системы',
        'Название ОС',
        'Код продукта',
        'Тип системы',
    ]

    return {
        'headers': main_data,
        'data': list(zip(os_prod_list, os_name_list, os_code_list, os_type_list)),
    }


def write_to_csv(input_file_list, output_file):
    data = get_data(input_file_list)

    print(data)

    writer = csv.writer(output_file)
    writer.writerow(data['headers'])
    writer.writerows(data['data'])


input_file_list = [
    'task1/info_1.txt',
    'task1/info_2.txt',
    'task1/info_3.txt',
]

output_file = 'task1/result.csv'

with open(output_file, 'wt', encoding='utf-8', newline='') as f:
    write_to_csv(input_file_list, f)
