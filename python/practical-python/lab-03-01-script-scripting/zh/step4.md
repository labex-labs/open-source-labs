# 定义函数

将与单个**任务**相关的所有代码放在一个地方是个好主意。使用函数。

```python
def read_prices(filename):
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

函数还简化了重复操作。

```python
oldprices = read_prices('oldprices.csv')
newprices = read_prices('newprices.csv')
```
