# Упражнение 5.7: Свойства и сеттеры

Измените атрибут `shares` так, чтобы значение хранилось в приватном атрибуте и использовались пара функций-свойств, чтобы гарантировать, что оно всегда устанавливается в целочисленное значение. Вот пример ожидаемого поведения:

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG',100,490.10)
>>> s.shares = 50
>>> s.shares = 'a lot'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: ожидается целое число
>>>
```
