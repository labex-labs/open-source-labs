# 处理数据

既然你已经学会了如何读取文件，下一步就是处理文件的每一行，以计算每笔股票交易的成本。这是在 Python 中处理数据的重要环节，因为它能让你从文件中提取有意义的信息。

文件中的每一行都遵循特定的格式：`[股票代码] [股数] [每股价格]`。要计算每笔股票交易的成本，你需要从每一行中提取股数和每股价格。然后，将这两个值相乘，得到该笔股票交易的成本。最后，将这笔成本累加到总成本中，以得出投资组合的总费用。

让我们修改 `pcost.py` 文件中的 `portfolio_cost()` 函数来实现这一点。以下是修改后的代码：

```python
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    # Open the file
    with open(filename, 'r') as file:
        # Read all lines in the file
        for line in file:
            # Strip any leading/trailing whitespace
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Split the line into fields
            fields = line.split()

            # Extract the relevant data
            # fields[0] is the stock symbol (which we don't need for the calculation)
            shares = int(fields[1])  # Number of shares (second field)
            price = float(fields[2])  # Price per share (third field)

            # Calculate the cost of this stock purchase
            cost = shares * price

            # Add to the total cost
            total_cost += cost

            # Print some debug information
            print(f'{fields[0]}: {shares} shares at ${price:.2f} = ${cost:.2f}')

    # Return the total cost
    return total_cost
```

让我们逐步分析这个修改后的函数的功能：

1. **去除空白字符**：使用 `strip()` 方法去除每行开头和结尾的空白字符。这样可以确保在将行拆分为字段时不会意外包含多余的空格。
2. **跳过空行**：如果某行是空的（即只包含空白字符），使用 `continue` 语句跳过该行。这有助于避免在尝试拆分空行时出错。
3. **将行拆分为字段**：使用 `split()` 方法根据空白字符将每行拆分为一个字段列表。这样就可以分别访问行中的每个部分。
4. **提取相关数据**：从字段列表中提取股数和每股价格。股数是第二个字段，每股价格是第三个字段。将这些值转换为适当的数据类型（股数为 `int` 类型，价格为 `float` 类型），以便进行算术运算。
5. **计算成本**：将股数乘以每股价格，计算出该笔股票交易的成本。
6. **累加到总成本**：将该笔股票交易的成本累加到总成本中。
7. **打印调试信息**：打印每笔股票交易的相关信息，帮助你了解程序的运行情况。这些信息包括股票代码、股数、每股价格和交易总成本。

现在，让我们运行代码，看看是否能正常工作。打开终端并运行以下命令：

```bash
python3 ~/project/pcost.py
```

运行命令后，你应该会看到每笔股票交易的详细信息，后面跟着投资组合的总成本。这个输出将帮助你验证函数是否正常工作，以及你是否准确计算了总成本。
