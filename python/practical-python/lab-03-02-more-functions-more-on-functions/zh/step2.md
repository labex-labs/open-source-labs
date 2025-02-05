# 默认参数

有时你希望某个参数是可选的。如果是这样，可以在函数定义中为其指定一个默认值。

```python
def read_prices(filename, debug=False):
  ...
```

如果指定了默认值，那么在函数调用时该参数就是可选的。

```python
d = read_prices('prices.csv')
e = read_prices('prices.dat', True)
```

**注意**：带有默认值的参数必须出现在参数列表的末尾（所有非可选参数要放在前面）。
