"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это необходимо в автоматическом,
а не ручном режиме, с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя методы
encode, decode или функцию bytes) и определить тип, содержимое и длину соответствующих переменных.
"""


def print_value_type_and_len(param):
    print('Type: ', type(param), ' Value: ', param, ' Len: ', len(param), sep='')


def convert_str_to_bytes(word):
    return eval(f"b'{word}'")


words = ['class', 'function', 'method']

for word in words:
    print_value_type_and_len(convert_str_to_bytes(word))
