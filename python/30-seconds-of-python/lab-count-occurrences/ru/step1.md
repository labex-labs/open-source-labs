# Подсчет вхождений

Напишите функцию `count_occurrences(lst, val)`, которая принимает список `lst` и значение `val` в качестве аргументов и возвращает количество вхождений `val` в `lst`. Ваша функция должна использовать встроенный метод `list.count()` для подсчета количества вхождений.

```python
def count_occurrences(lst, val):
  return lst.count(val)
```

```python
count_occurrences([1, 1, 2, 1, 2, 3], 1) # 3
```
