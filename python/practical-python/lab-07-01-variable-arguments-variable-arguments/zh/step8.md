# 练习7.4：参数传递

`fileparse.parse_csv()` 函数有一些用于更改文件分隔符和错误报告的选项。也许你想将这些选项暴露给上面的 `read_portfolio()` 函数。进行如下更改：

    def read_portfolio(filename, **opts):
        '''
        将股票投资组合文件读取为一个字典列表，字典包含键
        name、shares 和 price。
        '''
        with open(filename) as lines:
            portdicts = fileparse.parse_csv(lines,
                                            select=['name','shares','price'],
                                            types=[str,int,float],
                                            **opts)

        portfolio = [ Stock(**d) for d in portdicts ]
        return Portfolio(portfolio)

做出更改后，尝试读取一个包含一些错误的文件：

```python
>>> import report
>>> port = report.read_portfolio('missing.csv')
第4行：无法转换 ['MSFT', '', '51.23']
第4行：原因是 int() 无法将空字符串转换为十进制整数
第7行：无法转换 ['IBM', '', '70.44']
第7行：原因是 int() 无法将空字符串转换为十进制整数
>>>
```

现在，尝试抑制错误：

```python
>>> import report
>>> port = report.read_portfolio('missing.csv', silence_errors=True)
>>>
```
