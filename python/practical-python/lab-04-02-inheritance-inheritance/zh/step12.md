# 练习4.5：一个可扩展性问题

假设你想要修改 `print_report()` 函数，以支持多种不同的输出格式，如纯文本、HTML、CSV 或 XML。要做到这一点，你可能会尝试编写一个庞大的函数来处理所有事情。然而，这样做很可能会导致代码难以维护，变得一团糟。相反，这是一个使用继承的绝佳机会。

首先，关注创建表格所涉及的步骤。表格顶部是一组表头。之后是表格数据行。让我们把这些步骤提取出来，放到它们自己的类中。创建一个名为 `tableformat.py` 的文件，并定义以下类：

```python
# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        输出表格表头。
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        输出一行表格数据。
        '''
        raise NotImplementedError()
```

这个类什么也不做，但它为即将定义的其他类提供了一种设计规范。这样的类有时被称为“抽象基类”。

修改 `print_report()` 函数，使其接受一个 `TableFormatter` 对象作为输入，并调用它的方法来生成输出。例如，如下所示：

```python
# report.py
...

def print_report(reportdata, formatter):
    '''
    从 (name, shares, price, change) 元组列表中打印一个格式良好的表格。
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)
```

由于你在 `print_report()` 中添加了一个参数，你还需要修改 `portfolio_report()` 函数。将其修改为如下所示，以便它创建一个 `TableFormatter`：

```python
# report.py

import tableformat

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
    formatter = tableformat.TableFormatter()
    print_report(report, formatter)
```

运行这段新代码：

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
... 程序崩溃...
```

它应该会立即因 `NotImplementedError` 异常而崩溃。这并不太令人兴奋，但这正是我们所期望的。继续下一部分。
