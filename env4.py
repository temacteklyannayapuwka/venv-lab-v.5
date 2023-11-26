# Импортируем модуль os
import os
# Задаём значение переменной DEBUG
os.environ.setdefault('DEBUG', 'True')
# Проверяем значение переменной
if os.environ.get('DEBUG') == 'True':
   print('Debug mode is on')
else:
   print('Debug mode is off')