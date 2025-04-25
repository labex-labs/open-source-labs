# 练习 4.6：使用继承生成不同输出

你在（a）部分定义的 `TableFormatter` 类旨在通过继承进行扩展。实际上，这就是整个思路。为了说明这一点，定义一个如下的 `TextTableFormatter` 类：

```python
# tableformat.py
...
class TextTableFormatter(TableFormatter):
    '''
    以纯文本格式输出表格
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
```

将 `portfolio_report()` 函数修改如下并进行尝试：

```python
# report.py
...
def portfolio_report(portfoliofile, pricefile):
    '''
    根据投资组合和价格数据文件生成股票报告。
    '''
    # 读取数据文件
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # 创建报告数据
    report = make_report_data(portfolio, prices)

    # 打印输出
    formatter = tableformat.TextTableFormatter()
    print_report(report, formatter)
```

这应该会产生与之前相同的输出：

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
>>>
```

然而，让我们将输出改为其他格式。定义一个新的 `CSVTableFormatter` 类，以 CSV 格式输出：

```python
# tableformat.py
...
class CSVTableFormatter(TableFormatter):
    '''
    以 CSV 格式输出投资组合数据。
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))
```

将你的主程序修改如下：

```python
def portfolio_report(portfoliofile, pricefile):
    '''
    根据投资组合和价格数据文件生成股票报告。
    '''
    # 读取数据文件
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # 创建报告数据
    report = make_report_data(portfolio, prices)

    # 打印输出
    formatter = tableformat.CSVTableFormatter()
    print_report(report, formatter)
```

现在你应该会看到如下的 CSV 输出：

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
Name,Shares,Price,Change
AA,100,9.22,-22.98
IBM,50,106.28,15.18
CAT,150,35.46,-47.98
MSFT,200,20.89,-30.34
GE,95,13.48,-26.89
MSFT,50,20.89,-44.21
IBM,100,106.28,35.84
```

使用类似的思路，定义一个 `HTMLTableFormatter` 类，生成一个具有以下输出的表格：

    <tr><th>Name</th><th>Shares</th><th>Price</th><th>Change</th></tr>
    <tr><td>AA</td><td>100</td><td>9.22</td><td>-22.98</td></tr>
    <tr><td>IBM</td><td>50</td><td>106.28</td><td>15.18</td></tr>
    <tr><td>CAT</td><td>150</td><td>35.46</td><td>-47.98</td></tr>
    <tr><td>MSFT</td><td>200</td><td>20.89</td><td>-30.34</td></tr>
    <tr><td>GE</td><td>95</td><td>13.48</td><td>-26.89</td></tr>
    <tr><td>MSFT</td><td>50</td><td>20.89</td><td>-44.21</td></tr>
    <tr><td>IBM</td><td>100</td><td>106.28</td><td>35.84</td></tr>

通过修改主程序以创建一个 `HTMLTableFormatter` 对象而不是 `CSVTableFormatter` 对象来测试你的代码。
