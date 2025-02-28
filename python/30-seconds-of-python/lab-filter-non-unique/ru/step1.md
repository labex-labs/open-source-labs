# Фильтрация неуникальных значений списка

Напишите функцию на Python под названием `filter_non_unique(lst)`, которая принимает список в качестве аргумента и возвращает новый список, содержащий только уникальные значения. Чтобы решить эту задачу, вы можете следовать следующим шагам:

1. Используйте метод `collections.Counter`, чтобы получить количество каждого значения в списке.
2. Используйте списочное выражение, чтобы создать список, содержащий только уникальные значения.

```python
from collections import Counter

def filter_non_unique(lst):
  return [item for item, count in Counter(lst).items() if count == 1]
```

```python
filter_non_unique([1, 2, 2, 3, 4, 4, 5]) # [1, 3, 5]
```
