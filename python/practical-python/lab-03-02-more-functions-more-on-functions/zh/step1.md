# 调用函数

考虑以下函数：

```python
def read_prices(filename, debug):
 ...
```

你可以使用位置参数调用该函数：

    prices = read_prices('prices.csv', True)

或者你可以使用关键字参数调用该函数：

```python
prices = read_prices(filename='prices.csv', debug=True)
```
