# 练习 6.7：关注你的投资组合

修改 `follow.py` 程序，使其监视股票数据流，并仅打印出投资组合中那些股票的信息的报价器。例如：

```python
if __name__ == '__main__':
    import report

    portfolio = report.read_portfolio('portfolio.csv')

    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

注意：要使其正常工作，你的 `Portfolio` 类必须支持 `in` 运算符。请参阅练习 6.3，并确保你实现了 `__contains__()` 运算符。
