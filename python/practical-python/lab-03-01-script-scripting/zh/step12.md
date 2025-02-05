# 练习3.2：为程序执行创建一个顶级函数

将你程序的最后一部分打包成一个名为 `portfolio_report(portfolio_filename, prices_filename)` 的单一函数。让这个函数能够正常工作，以便以下函数调用能像之前一样生成报告：

```python
portfolio_report('/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv')
```

在这个最终版本中，你的程序将仅仅是一系列函数定义，最后跟着一个对 `portfolio_report()` 的单一函数调用（它会执行程序中涉及的所有步骤）。

通过将你的程序转换为一个单一函数，就可以很容易地在不同输入上运行它。例如，在运行你的程序后，交互式地尝试以下语句：

```python
>>> portfolio_report('/home/labex/project/portfolio2.csv', '/home/labex/project/prices.csv')
... 查看输出...
>>> files = ['/home/labex/project/portfolio.csv', '/home/labex/project/portfolio2.csv']
>>> for name in files:
        print(f'{name:-^43s}')
        portfolio_report(name, '/home/labex/project/prices.csv')
        print()

... 查看输出...
>>>
```
