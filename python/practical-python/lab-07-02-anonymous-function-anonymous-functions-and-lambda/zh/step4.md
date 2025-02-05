# 使用 lambda

- lambda 受到很大限制。
- 只允许单个表达式。
- 不允许使用 `if`、`while` 等语句。
- 最常见的用途是与 `sort()` 等函数一起使用。

读取一些股票投资组合数据并将其转换为列表：

```python
>>> import report
>>> portfolio = list(report.read_portfolio('portfolio.csv'))
>>> for s in portfolio:
        print(s)

Stock('AA', 100, 32.2)
Stock('IBM', 50, 91.1)
Stock('CAT', 150, 83.44)
Stock('MSFT', 200, 51.23)
Stock('GE', 95, 40.37)
Stock('MSFT', 50, 65.1)
Stock('IBM', 100, 70.44)
>>>
```
