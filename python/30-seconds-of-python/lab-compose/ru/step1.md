# Композиция функций

Напишите функцию под названием `compose(*fns)`, которая принимает одну или более функций в качестве аргументов и возвращает новую функцию, которая является результатом композиции входных функций с права налево. Последняя (самая правая) функция может принимать один или более аргументов; оставшиеся функции должны быть унарными.

```python
from functools import reduce

def compose(*fns):
  return reduce(lambda f, g: lambda *args: f(g(*args)), fns)
```

```python
add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)
multiply_and_add_5(5, 2) # 15
```
