# Найти максимальное значение списка на основе функции

Напишите функцию `max_by(lst, fn)`, которая принимает в качестве аргументов список `lst` и функцию `fn`. Функция должна сопоставить каждому элементу в `lst` значение с использованием заданной функции `fn`, а затем вернуть максимальное значение.

```python
def max_by(lst, fn):
  return max(map(fn, lst))
```

```python
max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 8
```
