# Найти соответствующий индекс

Напишите функцию `find_index(lst, fn)`, которая принимает список `lst` и тестирующую функцию `fn` в качестве аргументов. Функция должна возвращать индекс первого элемента в `lst`, для которого `fn` возвращает `True`.

```python
def find_index(lst, fn):
  return next(i for i, x in enumerate(lst) if fn(x))
```

```python
find_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 0
```
