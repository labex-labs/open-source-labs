# Функция для проверки наличия дубликатов в списке

Напишите функцию на Python под названием `has_duplicates(lst)`, которая принимает список в качестве аргумента и возвращает `True`, если список содержит какие-либо дубликаты элементов, в противном случае возвращает `False`.

Для решения этой проблемы вы можете следовать следующим шагам:

1. Преобразуйте список в множество, чтобы удалить дубликаты.
2. Сравните длину множества с длиной исходного списка.
3. Если длины равны, то список не содержит дубликатов, в противном случае он содержит дубликаты.

```python
def all_unique(lst):
  return len(lst) == len(set(lst))
```

```python
x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 2, 3, 4, 5]
all_unique(x) # True
all_unique(y) # False
```
