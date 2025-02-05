# 反向组合函数

编写一个函数 `compose_right`，它接受一个或多个函数作为参数，并返回一个执行从左到右函数组合的新函数。第一个（最左边的）函数可以接受一个或多个参数；其余函数必须是一元函数。

你的实现应该使用 `functools` 模块中的 `reduce` 函数来执行从左到右的函数组合。

```python
from functools import reduce

def compose_right(*fns):
  # 你的代码写在这里
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
