# Разница между списками

Напишите функцию на Python под названием `list_difference(a, b)`, которая принимает два списка в качестве аргументов и возвращает разницу между ними. Функция не должна фильтровать дубликаты значений. Чтобы решить данную задачу, вы можете следовать следующим шагам:

1. Создайте множество из второго списка `b`.
2. Используйте списочное выражение для первого списка `a`, чтобы оставить только те значения, которые не содержатся в ранее созданном множестве `_b`.
3. Верните результирующий список.

```python
def difference(a, b):
  _b = set(b)
  return [item for item in a if item not in _b]
```

```python
difference([1, 2, 3], [1, 2, 4]) # [3]
```
