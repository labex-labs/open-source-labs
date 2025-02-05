# 组合函数

编写一个名为 `compose(*fns)` 的函数，它接受一个或多个函数作为参数，并返回一个新函数，该新函数是从右到左组合输入函数的结果。最后一个（最右边的）函数可以接受一个或多个参数；其余函数必须是一元函数。

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
