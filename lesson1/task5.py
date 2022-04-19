"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип
на кириллице.
"""

import subprocess
import platform
import locale

default_locale = locale.getpreferredencoding()

param = '-n' if platform.system().lower() == 'windows' else '-c'
args = ['ping', param, '4', 'yandex.ru']
process = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in process.stdout:
    line = line.decode(default_locale).encode('utf-8')
    print(line.decode('utf-8'))
