# 练习7.3：创建实例列表

在你的 `report.py` 程序中，你使用如下代码创建了一个实例列表：

```python
def read_portfolio(filename):
    '''
    将股票投资组合文件读取为一个字典列表，字典包含键
    name、shares 和 price。
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                               select=['name','shares','price'],
                               types=[str,int,float])

    portfolio = [ Stock(d['name'], d['shares'], d['price'])
                  for d in portdicts ]
    return Portfolio(portfolio)
```

你可以使用 `Stock(**d)` 来简化这段代码。进行这个更改。
