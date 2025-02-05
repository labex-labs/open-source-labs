# 关键字可变参数（\*\*kwargs）

一个函数也可以接受任意数量的关键字参数。例如：

```python
def f(x, y, **kwargs):
...
```

函数调用：

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

额外的关键字参数会以字典的形式传递。

```python
def f(x, y, **kwargs):
    # x -> 2
    # y -> 3
    # kwargs -> { 'flag': True,'mode': 'fast', 'header': 'debug' }
```
