# 局部变量

在函数内部赋值的变量是私有的。

```python
def read_portfolio(filename):
    portfolio = []
    for line in open(filename):
        fields = line.split(',')
        s = (fields[0], int(fields[1]), float(fields[2]))
        portfolio.append(s)
    return portfolio
```

在这个例子中，`filename`、`portfolio`、`line`、`fields` 和 `s` 都是局部变量。在函数调用之后，这些变量不会被保留或访问。

```python
>>> stocks = read_portfolio('portfolio.csv')
>>> fields
Traceback (most recent call last):
File "<stdin>", line 1, in?
NameError: name 'fields' is not defined
>>>
```

局部变量也不会与其他地方的变量冲突。
