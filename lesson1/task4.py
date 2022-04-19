"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""


def print_value_and_type(word):
    print('Type: ', type(word), ' Value: ', word, sep='')


words = ['разработка', 'администрирование', 'protocol', 'standard']

print('=' * 10, ' Source words ', '=' * 10)
for word in words:
    print_value_and_type(word)

words_bytes = []

for word in words:
    words_bytes.append(word.encode('utf-8'))

print('=' * 10, ' Converted words to bytes ', '=' * 10)
for item in words_bytes:
    print_value_and_type(item)

words_restored = []

for word in words_bytes:
    words_restored.append(word.decode('utf-8'))

print('=' * 10, ' Restored wordds ', '=' * 10)
for word in words_restored:
    print_value_and_type(word)
