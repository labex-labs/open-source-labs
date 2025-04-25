# 练习 4.7：多态性的实际应用

面向对象编程的一个主要特性是，你可以将一个对象插入到程序中，它就能正常工作，而无需更改任何现有代码。例如，如果你编写了一个期望使用 `TableFormatter` 对象的程序，无论你实际提供的是哪种 `TableFormatter`，它都能正常运行。这种行为有时被称为“多态性”。

一个潜在的问题是弄清楚如何允许用户选择他们想要的格式化器。直接使用类名，如 `TextTableFormatter`，通常很麻烦。因此，你可能会考虑一些简化的方法。也许你可以在代码中嵌入一个 `if` 语句，如下所示：

```python
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    根据投资组合和价格数据文件生成股票报告。
    '''
    # 读取数据文件
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # 创建报告数据
    report = make_report_data(portfolio, prices)

    # 打印输出
    if fmt == 'txt':
        formatter = tableformat.TextTableFormatter()
    elif fmt == 'csv':
        formatter = tableformat.CSVTableFormatter()
    elif fmt == 'html':
        formatter = tableformat.HTMLTableFormatter()
    else:
        raise RuntimeError(f'未知格式 {fmt}')
    print_report(report, formatter)
```

在这段代码中，用户指定一个简化的名称，如 `'txt'` 或 `'csv'` 来选择一种格式。然而，像那样在 `portfolio_report()` 函数中放置一个大型 `if` 语句是最好的主意吗？也许将那段代码移到其他地方的一个通用函数中会更好。

在 `tableformat.py` 文件中，添加一个函数 `create_formatter(name)`，它允许用户根据输出名称，如 `'txt'`、`'csv'` 或 `'html'` 创建一个格式化器。修改 `portfolio_report()`，使其如下所示：

```python
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    根据投资组合和价格数据文件生成股票报告。
    '''
    # 读取数据文件
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # 创建报告数据
    report = make_report_data(portfolio, prices)

    # 打印输出
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
```

尝试使用不同的格式调用该函数，以确保它能正常工作。
