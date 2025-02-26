# Упражнение 7.2: Передача кортежей и словарей в качестве аргументов

Предположим, что вы прочитали некоторые данные из файла и получили кортеж такого вида:

```python
>>> data = ('GOOG', 100, 490.1)
>>>
```

Теперь, предположим, что вы хотели создать объект `Stock` из этих данных. Если вы попытаетесь передать `data` напрямую, это не сработает:

```python
>>> from stock import Stock
>>> s = Stock(data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Stock.__init__() missing 2 required positional arguments:'shares' and 'price'
>>>
```

Это легко исправить, используя `*data` вместо этого. Попробуйте это:

```python
>>> s = Stock(*data)
>>> s
Stock('GOOG', 100, 490.1)
>>>
```

Если у вас есть словарь, вы можете использовать `**` вместо этого. Например:

```python
>>> data = { 'name': 'GOOG','shares': 100, 'price': 490.1 }
>>> s = Stock(**data)
Stock('GOOG', 100, 490.1)
>>>
```
