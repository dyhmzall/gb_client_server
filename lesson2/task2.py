"""
2. Задание на закрепление знаний по модулю json.
Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными.
Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;

Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import chardet
import json


def get_content_utf(content):
    return content.decode(chardet.detect(content)['encoding']).encode('utf-8').decode('utf-8')


def write_order_to_json(item, quantity, price, buyer, date):
    order = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }

    with open('task2/orders.json', 'rb') as f:
        content = get_content_utf(f.read())
        orders = json.loads(content)

    print(orders)

    orders['orders'].append(order)

    print(orders)

    with open('task2/orders.json', 'wt', encoding='utf-8') as f:
        json.dump(orders, f, sort_keys=True, indent=4, ensure_ascii=False)


write_order_to_json('кресло', 100, 123.45, 'Джон Смит', '26.04.2022')
