# Упражнение 5.6: Простые свойства

Свойства - это полезный способ добавить "вычисляемые атрибуты" к объекту. В `stock.py` вы создали объект `Stock`. Обратите внимание, что в вашем объекте есть небольшая несовместимость в том, как извлекаются разные виды данных:

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.shares
100
>>> s.price
490.1
>>> s.cost()
49010.0
>>>
```

В частности, обратите внимание, как вам приходится добавлять дополнительные круглые скобки к `cost`, потому что это метод.

Вы можете избавиться от дополнительных круглых скобок при вызове `cost()`, если превратить его в свойство. Возьмите класс `Stock` и модифицируйте его так, чтобы расчет стоимости работал следующим образом:

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.cost
49010.0
>>>
```

Попробуйте вызвать `s.cost()` в качестве функции и заметьте, что это уже не работает, так как `cost` теперь определено как свойство.

```python
>>> s.cost()
... не работает...
>>>
```

Внесение этого изменения, вероятно, сломает ваш ранний `pcost.py`-программу. Возможно, вам придется вернуться и убрать круглые скобки из метода `cost()`.
