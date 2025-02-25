# Каррированная функция

Напишите функцию `curry(fn, *args)`, которая осуществляет каррирование заданной функции `fn`. Функция должна возвращать новую функцию, которая ведет себя аналогично `fn` с заданными аргументами `args`, частично примененными.

```python
from functools import partial

def curry(fn, *args):
  return partial(fn, *args)
```

```python
add = lambda x, y: x + y
add10 = curry(add, 10)
add10(20) # 30
```
