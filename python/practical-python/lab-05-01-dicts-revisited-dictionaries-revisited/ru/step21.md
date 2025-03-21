# Упражнение 5.4: Связанные методы

Некоторый тонкий аспект Python заключается в том, что вызов метода на самом деле включает два шага и что-то, что называется связанным методом. Например:

```python
>>> s = goog.sell
>>> s
<bound method Stock.sell of Stock('GOOG', 100, 490.1)>
>>> s(25)
>>> goog.shares
75
>>>
```

Связанные методы на самом деле содержат все элементы, необходимые для вызова метода. Например, они хранят запись о функции, реализующей метод:

```python
>>> s.__func__
<function sell at 0x10049af50>
>>>
```

Это то же значение, что и в словаре `Stock`.

```python
>>> Stock.__dict__['sell']
<function sell at 0x10049af50>
>>>
```

Связанные методы также запоминают экземпляр, который является аргументом `self`.

```python
>>> s.__self__
Stock('GOOG',75,490.1)
>>>
```

Когда вы вызываете функцию с использованием `()`, все элементы объединяются. Например, вызов `s(25)` на самом деле делает это:

```python
>>> s.__func__(s.__self__, 25)    # То же, что и s(25)
>>> goog.shares
50
>>>
```
