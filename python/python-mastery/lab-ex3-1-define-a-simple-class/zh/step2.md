# 从 CSV 文件中读取投资组合

在这一步中，我们将创建一个函数，用于从 CSV 文件中读取股票数据，并返回一个 `Stock` 对象列表。`Stock` 对象代表股票持仓，完成这一步后，你将能够从 CSV 文件中读取股票投资组合。

## 理解 CSV 文件

CSV 是逗号分隔值（Comma-Separated Values）的缩写，它是一种非常常见的存储表格数据的格式。你可以把它想象成一个简单的电子表格。CSV 文件中的每一行代表一行数据，行内的各列由逗号分隔。通常，CSV 文件的第一行包含表头，这些表头描述了每列数据的类型。例如，在一个股票投资组合的 CSV 文件中，表头可能是 “名称”、“股数” 和 “价格”。

## 实现说明

1. 首先，在你的代码编辑器中打开 `stock.py` 文件。如果已经打开了，那就很好；如果没有，找到并打开它。我们将在这个文件中添加新的函数。

2. 打开 `stock.py` 文件后，查找注释 `# TODO: Add read_portfolio(filename) function here`。这个注释是一个占位符，指示我们应该在哪里添加新的函数。

3. 在该注释下方，添加以下函数。这个函数名为 `read_portfolio`，它接受一个文件名作为参数。该函数的目的是读取 CSV 文件，提取股票数据，并创建一个 `Stock` 对象列表。

```python
def read_portfolio(filename):
    """
    Read a CSV file containing portfolio data and return a list of Stock objects.

    Args:
        filename (str): Path to the CSV file

    Returns:
        list: A list of Stock objects
    """
    portfolio = []

    with open(filename, 'r') as f:
        headers = next(f).strip().split(',')  # Skip the header line

        for line in f:
            row = line.strip().split(',')
            name = row[0]
            shares = int(row[1])
            price = float(row[2])

            # Create a Stock object and add it to the portfolio list
            stock = Stock(name, shares, price)
            portfolio.append(stock)

    return portfolio
```

让我们来详细分析这个函数的功能。首先，它创建了一个名为 `portfolio` 的空列表。然后，它以只读模式打开 CSV 文件。`next(f)` 语句跳过了第一行，即表头行。之后，它遍历文件中的每一行。对于每一行，它将行分割成一个值列表，提取名称、股数和价格，创建一个 `Stock` 对象，并将其添加到 `portfolio` 列表中。最后，它返回 `portfolio` 列表。

4. 添加函数后，保存 `stock.py` 文件。你可以通过按下键盘上的 `Ctrl+S` 组合键，或者在代码编辑器的菜单中选择 “文件 > 保存” 来完成保存操作。保存文件可确保你的更改得以保留。

5. 现在，我们需要测试 `read_portfolio` 函数。创建一个名为 `test_portfolio.py` 的新 Python 脚本。这个脚本将从 `stock.py` 文件中导入 `read_portfolio` 函数，从 CSV 文件中读取投资组合，并打印投资组合中每只股票的信息。

```python
# test_portfolio.py
from stock import read_portfolio

# Read the portfolio from the CSV file
portfolio = read_portfolio('portfolio.csv')

# Print information about each stock
for stock in portfolio:
    print(f"Name: {stock.name}, Shares: {stock.shares}, Price: ${stock.price:.2f}")

# Print the total number of stocks in the portfolio
print(f"\nTotal number of stocks in portfolio: {len(portfolio)}")
```

在这个脚本中，我们首先导入 `read_portfolio` 函数。然后，我们使用文件名 `portfolio.csv` 调用该函数，以获取 `Stock` 对象列表。接着，我们遍历该列表并打印每只股票的信息。最后，我们打印投资组合中股票的总数。

6. 要运行测试脚本，请打开终端或命令提示符，导航到 `test_portfolio.py` 文件所在的目录，并运行以下命令：

```bash
python3 test_portfolio.py
```

如果一切正常，你应该会看到输出列出了 `portfolio.csv` 文件中的所有股票，以及它们的名称、股数和价格。你还应该会看到投资组合中股票的总数。

```
Name: AA, Shares: 100, Price: $32.20
Name: IBM, Shares: 50, Price: $91.10
Name: CAT, Shares: 150, Price: $83.44
Name: MSFT, Shares: 200, Price: $51.23
Name: GE, Shares: 95, Price: $40.37
Name: MSFT, Shares: 50, Price: $65.10
Name: IBM, Shares: 100, Price: $70.44

Total number of stocks in portfolio: 7
```

这个输出确认了你的 `read_portfolio` 函数能够正确读取 CSV 文件，并根据其中的数据创建 `Stock` 对象。
