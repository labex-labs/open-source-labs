# 打开并读取文件

在这一步中，你将学习如何在 Python 中打开并读取文件。文件输入/输出（I/O）是编程中的一个基本概念。它允许你的程序与外部文件（如文本文件、CSV 文件等）进行交互。在 Python 中，处理文件最常用的方法之一是使用 `open()` 函数。

`open()` 函数用于在 Python 中打开文件。它接受两个重要参数。第一个参数是你要打开的文件的名称。第二个参数是你打开文件的模式。当你要读取文件时，使用模式 `'r'`。这告诉 Python 你只想读取文件的内容，而不做任何修改。

现在，让我们在 `pcost.py` 文件中添加一些代码来打开并读取 `portfolio.dat` 文件。在代码编辑器中打开 `pcost.py` 文件，并添加以下代码：

```python
# pcost.py
# Calculate the total cost of a portfolio of stocks

def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    # Open the file
    with open(filename, 'r') as file:
        # Read all lines in the file
        for line in file:
            print(line)  # Just for debugging, to see what we're reading

    # Return the total cost
    return total_cost

# Call the function with the portfolio file
total_cost = portfolio_cost('portfolio.dat')
print(f'Total cost: ${total_cost}')
```

让我们来详细分析这段代码的功能：

1. 首先，我们定义了一个名为 `portfolio_cost()` 的函数。这个函数接受一个文件名作为输入参数。该函数的目的是根据文件中的数据计算股票投资组合的总成本。
2. 在函数内部，我们使用 `open()` 函数以只读模式打开指定的文件。这里使用 `with` 语句确保在读取完文件后正确关闭文件。这是避免资源泄漏的良好实践。
3. 然后，我们使用 `for` 循环逐行读取文件。对于文件中的每一行，我们将其打印出来。这只是为了调试，以便我们可以查看从文件中读取的数据。
4. 读取完文件后，函数返回总成本。目前，总成本被设置为 0.0，因为我们还没有实现实际的计算。
5. 在函数外部，我们使用文件名 `'portfolio.dat'` 调用 `portfolio_cost()` 函数。这意味着我们要求该函数根据 `portfolio.dat` 文件中的数据计算总成本。
6. 最后，我们使用 f-string 打印总成本。

现在，让我们运行这段代码，看看它的效果。你可以在终端中使用以下命令运行 Python 文件：

```bash
python3 ~/project/pcost.py
```

当你运行此命令时，你应该会在终端上看到 `portfolio.dat` 文件的每一行被打印出来，后面跟着总成本，目前总成本被设置为 0.0。这个输出可以帮助你验证文件是否被正确读取。
