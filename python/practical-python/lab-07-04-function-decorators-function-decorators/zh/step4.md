# 装饰器

在 Python 中，为函数添加包装器是非常常见的操作。正因如此，Python 为此提供了一种特殊的语法。

```python
def add(x, y):
    return x + y
add = logged(add)

# 特殊语法
@logged
def add(x, y):
    return x + y
```

这种特殊语法执行的步骤与上述代码完全相同。装饰器只是一种新的语法形式。它用于“装饰”函数。
