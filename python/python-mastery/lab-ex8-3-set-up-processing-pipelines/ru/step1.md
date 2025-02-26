# Пример корутины

Начало работы с корутинами может быть немного сложным. Вот пример программы, которая выполняет ту же задачу, что и упражнение 8.2, но с использованием корутин. Скопируйте эту программу в файл с именем `cofollow.py`.

```python
# cofollow.py
import os
import time

# Источник данных
def follow(filename,target):
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line!= '':
                target.send(line)
            else:
                time.sleep(0.1)

# Декоратор для функций-орутин
from functools import wraps

def consumer(func):
    @wraps(func)
    def start(*args,**kwargs):
        f = func(*args,**kwargs)
        f.send(None)
        return f
    return start

# Примерная корутина
@consumer
def printer():
    while True:
        item = yield     # Получить элемент, отправленный мне
        print(item)

# Пример использования
if __name__ == '__main__':
    follow('stocklog.csv',printer())
```

Запустите эту программу и убедитесь, что она выводит результат. Убедитесь, что вы понимаете, как разные части программы соединены между собой.
