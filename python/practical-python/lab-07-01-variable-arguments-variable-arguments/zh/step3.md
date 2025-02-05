# 两者结合

一个函数也可以接受任意数量的可变关键字参数和非关键字参数。

```python
def f(*args, **kwargs):
  ...
```

函数调用：

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

参数被分为位置参数和关键字参数两部分

```python
def f(*args, **kwargs):
    # args = (2, 3)
    # kwargs -> { 'flag': True,'mode': 'fast', 'header': 'debug' }
  ...
```

这个函数可以接受任意组合的位置参数或关键字参数。它有时用于编写包装器，或者当你想要将参数传递给另一个函数时使用。
