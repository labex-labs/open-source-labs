# 日志记录示例

考虑一个函数。

```python
def add(x, y):
    return x + y
```

现在，考虑为该函数添加了一些日志记录后的情况。

```python
def add(x, y):
    print('Calling add')
    return x + y
```

现在来看另一个同样添加了一些日志记录的函数。

```python
def sub(x, y):
    print('Calling sub')
    return x - y
```
