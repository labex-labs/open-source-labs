# Упражнение 5.8: Добавление слотов

Измените класс `Stock` так, чтобы он имел атрибут `__slots__`. Затем, проверьте, что нельзя добавить новые атрибуты:

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.blah = 42
... посмотрите, что произойдет...
>>>
```

Когда вы используете `__slots__`, Python использует более эффективное внутреннее представление объектов. Что произойдет, если вы попытаетесь проверить внутренний словарь `s` выше?

```python
>>> s.__dict__
... посмотрите, что произойдет...
>>>
```

Следует отметить, что `__slots__` наиболее часто используется как оптимизация для классов, которые служат в качестве структур данных. Использование слотов сделает такие программы использовать намного меньше памяти и работать немного быстрее. Однако вы, вероятно, должны избегать использования `__slots__` для большинства других классов.
