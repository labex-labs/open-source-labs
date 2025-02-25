# Композиция функций в обратном порядке

Напишите функцию `compose_right`, которая принимает одну или более функций в качестве аргументов и возвращает новую функцию, которая выполняет композицию функций слева направо. Первая (самая левая) функция может принимать один или более аргументов; оставшиеся функции должны быть унарными.

Ваше реализация должна использовать функцию `reduce` из модуля `functools` для выполнения композиции функций слева направо.

```python
from functools import reduce

def compose_right(*fns):
  # ваш код здесь
```

```python
from functools import reduce

def compose_right(*fns):
  return reduce(lambda f, g: lambda *args: g(f(*args)), fns)
```

```python
add = lambda x, y: x + y
square = lambda x: x * x
add_and_square = compose_right(add, square)
add_and_square(1, 2) # 9
```
