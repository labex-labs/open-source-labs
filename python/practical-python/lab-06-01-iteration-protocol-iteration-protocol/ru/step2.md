# Итерация: Протокол

Рассмотрим оператор `for`.

```python
for x in obj:
    # statements
```

Что происходит "под капотом"?

```python
_iter = obj.__iter__()        # Получаем объект-итератор
while True:
    try:
        x = _iter.__next__()  # Получаем следующий элемент
        # statements...
    except StopIteration:     # Больше элементов нет
        break
```

Все объекты, которые работают с циклом `for`, реализуют этот низкоуровневый протокол итерации.

Пример: Ручная итерация по списку.

```python
>>> x = [1,2,3]
>>> it = x.__iter__()
>>> it
<listiterator object at 0x590b0>
>>> it.__next__()
1
>>> it.__next__()
2
>>> it.__next__()
3
>>> it.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in? StopIteration
>>>
```
