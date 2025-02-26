# Ваш первый декоратор

Для начала работы с декораторами напишите _очень_ простую функцию-декоратор, которая просто выводит сообщение каждый раз, когда функция вызывается. Создайте файл `logcall.py` и определите следующую функцию:

```python
# logcall.py

def logged(func):
    print('Adding logging to', func.__name__)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

Теперь создайте отдельный файл `sample.py` и примените его к нескольким определениям функций:

```python
# sample.py

from logcall import logged

@logged
def add(x,y):
    return x+y

@logged
def sub(x,y):
    return x-y
```

Протестируйте свой код следующим образом:

```python
>>> import sample
Adding logging to add
Adding logging to sub
>>> sample.add(3,4)
Calling add
7
>>> sample.sub(2,3)
Calling sub
-1
>>>
```
