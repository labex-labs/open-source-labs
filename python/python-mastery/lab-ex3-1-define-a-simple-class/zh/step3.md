# 格式化并打印投资组合数据

在这一步中，我们将创建一个函数，帮助我们以结构良好的表格形式展示投资组合数据。投资组合是股票的集合，以清晰易读的方式呈现这些数据非常重要。这就是 `print_portfolio(portfolio)` 函数的用武之地。该函数将投资组合作为输入，并以带有表头且格式对齐的表格形式展示。

## Python 中的字符串格式化

在 Python 中，有多种字符串格式化的方法。字符串格式化是一项关键技能，因为它能让你以更有条理且用户友好的方式呈现数据。

- `%` 运算符是一种较旧的字符串格式化方式。它就像一个模板，你可以将值插入到字符串的特定位置。
- `str.format()` 方法是另一种方式。它在字符串格式化方面提供了更多的灵活性和更简洁的语法。
- f - 字符串是 Python 3.6 及更高版本引入的特性。它们非常方便，因为允许你在字符串字面量中嵌入表达式。

在这个练习中，我们将使用 `%` 运算符。当你想要创建固定宽度的列时，它特别有用，而这正是我们的投资组合表格所需要的。

## 实现说明

1. 首先，在你的编辑器中打开 `stock.py` 文件。如果已经打开了，那就很好。我们将在这个文件中编写 `print_portfolio` 函数。

2. 打开文件后，查找 `# TODO: Add print_portfolio(portfolio) function here` 注释。这个注释是一个标记，指示我们应该在哪里添加新函数。

3. 在该注释下方，添加以下函数：

```python
def print_portfolio(portfolio):
    """
    Print the portfolio data in a nicely formatted table.

    Args:
        portfolio (list): A list of Stock objects
    """
    # Print the header row
    print('%10s %10s %10s' % ('name', 'shares', 'price'))

    # Print a separator line
    print('-' * 10 + ' ' + '-' * 10 + ' ' + '-' * 10)

    # Print each stock in the portfolio
    for stock in portfolio:
        print('%10s %10d %10.2f' % (stock.name, stock.shares, stock.price))
```

这个函数首先打印表格的表头行，然后打印分隔线，最后遍历投资组合中的每只股票，并以格式化的方式打印其详细信息。

4. 添加函数后，保存文件。你可以通过按下 `Ctrl+S` 组合键，或者在菜单中选择“文件 > 保存”来完成保存操作。保存文件可确保你的更改得以保留。

5. 现在，我们需要测试我们的函数。创建一个名为 `test_print.py` 的新文件。这个文件将作为我们的测试脚本。在其中添加以下代码：

```python
# test_print.py
from stock import read_portfolio, print_portfolio

# Read the portfolio from the CSV file
portfolio = read_portfolio('portfolio.csv')

# Print the portfolio as a formatted table
print_portfolio(portfolio)
```

这个脚本从 `stock.py` 文件中导入 `read_portfolio` 和 `print_portfolio` 函数。然后，它从 CSV 文件中读取投资组合数据，并使用我们新创建的 `print_portfolio` 函数来展示这些数据。

6. 最后，运行测试脚本。打开你的终端并输入以下命令：

```bash
python3 test_print.py
```

如果一切正常，你应该会看到如下输出：

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

这个输出确认了你的 `print_portfolio` 函数按预期工作。它将投资组合数据格式化为带有表头且列对齐的表格，使其易于阅读。

## 理解字符串格式化

让我们仔细看看 `print_portfolio` 函数中的字符串格式化是如何工作的。

- `%10s` 用于格式化字符串。`10` 表示字段的宽度，`s` 代表字符串。它将字符串在宽度为 10 的字段内右对齐。
- `%10d` 用于格式化整数。`10` 是字段宽度，`d` 表示整数。它也将整数在宽度为 10 的字段内右对齐。
- `%10.2f` 用于格式化浮点数。`10` 是字段宽度，`.2` 指定我们要将浮点数显示为保留 2 位小数。它将浮点数在宽度为 10 的字段内右对齐。

这种格式化方式确保了表格中的所有列都能正确对齐，从而使输出更易于阅读和理解。
