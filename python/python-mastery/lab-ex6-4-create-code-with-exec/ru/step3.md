# Именованные кортежи

В упражнении 2.1 вы экспериментировали с объектами `namedtuple` из модуля `collections`. Просто чтобы освежить вашу память, вот, как они работали:

```python
>>> from collections import namedtuple
>>> Stock = namedtuple('Stock', ['name','shares', 'price'])
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s[1]
100
>>>
```

Под капотом функция `namedtuple()` создает код в виде строки и выполняет его с использованием `exec()`. Посмотрите на код и восхищайтесь:

```python
>>> import inspect
>>> print(inspect.getsource(namedtuple))
... посмотрите на вывод...
>>>
```
