# Импортируем модуль os
import os
# Проверяем значение переменной среды
if os.environ.get('DEBUG') == 'True':
   print('Debug mode is on')
else:
   print('Debug mode is off')