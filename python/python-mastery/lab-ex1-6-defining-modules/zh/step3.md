# 创建你自己的模块

既然你已经了解了如何使用现有的模块，那么现在是时候从头开始创建一个新模块了。在 Python 中，模块是一个包含 Python 定义和语句的文件。它允许你将代码组织成可复用且易于管理的部分。通过创建自己的模块，你可以将相关的函数和变量组合在一起，使你的代码更具模块化，也更易于维护。

## 创建一个报告模块

让我们创建一个简单的模块来生成股票报告。这个模块将包含读取投资组合文件并打印投资组合中股票格式化报告的函数。

1. 首先，我们需要创建一个名为 `report.py` 的新文件。为此，我们将使用命令行。导航到你主目录下的 `project` 目录，并使用 `touch` 命令创建该文件。

```bash
cd ~/project
touch report.py
```

2. 现在，在你喜欢的文本编辑器中打开 `report.py` 文件，并添加以下代码。这段代码定义了两个函数和一个主程序块。

```python
# report.py

def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with
    keys: name, shares, price
    """
    portfolio = []
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                stock = {
                    'name': fields[0],
                    'shares': int(fields[1]),
                    'price': float(fields[2])
                }
                portfolio.append(stock)
            except (ValueError, IndexError):
                print(f"Couldn't parse: {line}")
    return portfolio

def print_report(portfolio):
    """
    Print a report showing the stock name, shares, price, and total value
    """
    print("Name    Shares    Price    Value")
    print("-" * 40)
    total_value = 0.0
    for stock in portfolio:
        value = stock['shares'] * stock['price']
        total_value += value
        print(f"{stock['name']:6s} {stock['shares']:9d} {stock['price']:9.2f} {value:9.2f}")
    print("-" * 40)
    print(f"Total Value: {total_value:16.2f}")

if __name__ == "__main__":
    portfolio = read_portfolio('portfolio.dat')
    print_report(portfolio)
```

`read_portfolio` 函数读取包含股票信息的文件，并返回一个字典列表，其中每个字典代表一支股票，包含 `name`、`shares` 和 `price` 键。`print_report` 函数接受一个投资组合（股票字典列表），并打印一个格式化的报告，显示股票名称、股数、价格和总价值。末尾的主程序块在文件直接执行时运行，它读取投资组合文件并打印报告。

3. 添加代码后，保存并退出编辑器。

## 测试你的模块

让我们测试我们的新模块，确保它按预期工作。

1. 首先，我们将从命令行直接运行脚本。这将执行 `report.py` 文件中的主程序块。

```bash
python3 report.py
```

你应该会看到一个格式化的报告，显示投资组合中的股票及其价值。该报告包括股票名称、股数、价格和总价值，以及整个投资组合的总价值。

```
Name    Shares    Price    Value
----------------------------------------
AA         100     32.20   3220.00
IBM         50     91.10   4555.00
CAT        150     83.44  12516.00
MSFT       200     51.23  10246.00
GE          95     40.37   3835.15
MSFT        50     65.10   3255.00
IBM        100     70.44   7044.00
----------------------------------------
Total Value:         44671.15
```

2. 接下来，我们将从 Python 解释器中使用该模块。在终端中运行 `python3` 命令启动 Python 解释器。

```bash
python3
```

解释器启动后，我们可以导入 `report` 模块并使用其函数。

```python
import report
portfolio = report.read_portfolio('portfolio.dat')
len(portfolio)  # Should return 7, the number of stocks
portfolio[0]    # First stock in the portfolio
```

`import report` 语句使 `report.py` 文件中定义的函数和变量在当前 Python 会话中可用。然后，我们使用 `read_portfolio` 函数读取投资组合文件，并将结果存储在 `portfolio` 变量中。`len(portfolio)` 语句返回投资组合中的股票数量，`portfolio[0]` 返回投资组合中的第一支股票。

你应该会看到以下输出：

```
7
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

3. 现在，让我们使用导入的模块自己计算投资组合的总成本。我们将遍历投资组合中的股票，并将每支股票的总价值相加。

```python
total = 0.0
for stock in portfolio:
    total += stock['shares'] * stock['price']
print(total)
```

输出应该是 `44671.15`，这与 `print_report` 函数打印的总价值相同。

4. 最后，让我们为特定类型的股票创建一个自定义报告。我们将过滤投资组合，只包含 IBM 股票，然后使用 `print_report` 函数为这些股票打印报告。

```python
ibm_stocks = [stock for stock in portfolio if stock['name'] == 'IBM']
report.print_report(ibm_stocks)
```

这应该会打印一个只显示 IBM 股票及其价值的报告。

```
Name    Shares    Price    Value
----------------------------------------
IBM         50     91.10   4555.00
IBM        100     70.44   7044.00
----------------------------------------
Total Value:         11599.00
```

5. 测试完成后，运行 `exit()` 命令退出 Python 解释器。

```python
exit()
```

你现在已经成功创建并使用了自己的 Python 模块，它结合了函数和一个仅在文件直接执行时运行的主程序块。这种模块化的编程方法允许你复用代码，使你的项目更有条理且易于维护。
