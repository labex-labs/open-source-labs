# 文档字符串

以文档字符串的形式包含文档是个好习惯。文档字符串是紧跟在函数名之后编写的字符串。它们为 `help()`、集成开发环境（IDE）和其他工具提供信息。

```python
def read_prices(filename):
    '''
    从包含名称、价格数据的 CSV 文件中读取价格
    '''
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

编写文档字符串的一个好习惯是用一句话简短总结函数的功能。如果需要更多信息，可以包含一个简短的使用示例以及对参数更详细的描述。
