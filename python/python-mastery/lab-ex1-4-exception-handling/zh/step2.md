# 添加错误处理

当你处理现实世界的数据时，遇到数据不一致或错误是非常常见的。例如，数据可能存在缺失值、格式不正确或其他问题。Python 提供了异常处理机制来优雅地处理这些情况。异常处理能让你的程序即使遇到错误也能继续运行，而不是突然崩溃。

## 理解问题

让我们看一下 `portfolio3.dat` 文件。这个文件包含了一些投资组合的数据，如股票代码、股数和每股价格。要查看这个文件的内容，我们可以使用以下命令：

```bash
cat /home/labex/project/portfolio3.dat
```

当你运行这个命令时，你会注意到文件中的某些行在股数的位置使用了破折号 (`-`) 而不是数字。以下是你可能看到的示例：

```
AA 100 32.20
IBM 50 91.10
C - 53.08
...
```

如果我们尝试在这个文件上运行当前的代码，程序将会崩溃。原因是我们的代码期望将股数转换为整数，但无法将破折号 (`-`) 转换为整数。让我们尝试运行代码，看看会发生什么：

```bash
python3 -c "import sys; sys.path.append('/home/labex/project'); from pcost import portfolio_cost; print(portfolio_cost('/home/labex/project/portfolio3.dat'))"
```

你会看到类似这样的错误消息：

```
ValueError: invalid literal for int() with base 10: '-'
```

这个错误发生是因为 Python 在尝试执行 `int(fields[1])` 时，无法将 `-` 字符转换为整数。

## 异常处理简介

Python 的异常处理使用 `try` 和 `except` 块。`try` 块包含可能引发异常的代码。异常是程序执行过程中发生的错误。`except` 块包含在 `try` 块中发生异常时将执行的代码。

以下是 `try` 和 `except` 块如何工作的示例：

```python
try:
    # 可能引发异常的代码
    result = risky_operation()
except ExceptionType as e:
    # 处理异常的代码
    print(f"An error occurred: {e}")
```

当 Python 执行 `try` 块中的代码时，如果发生异常，执行会立即跳转到匹配的 `except` 块。`except` 块中的 `ExceptionType` 指定了我们要处理的异常类型。变量 `e` 包含有关异常的信息，如错误消息。

## 使用异常处理修改函数

让我们更新 `pcost.py` 文件以处理数据中的错误。我们将使用 `try` 和 `except` 块跳过包含错误数据的行，并显示警告消息。

```python
def portfolio_cost(filename):
    """
    计算投资组合文件的总成本（股数 * 价格）
    通过跳过包含错误数据的行并显示警告来处理这些行。

    参数：
        filename: 投资组合文件的名称

    返回：
        投资组合的总成本，以浮点数表示
    """
    total_cost = 0.0

    # 打开文件并逐行读取
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                # 提取数据（股票代码、股数、价格）
                shares = int(fields[1])
                price = float(fields[2])
                # 将成本累加到总成本中
                total_cost += shares * price
            except ValueError as e:
                # 为无法解析的行打印警告
                print(f"Couldn't parse: '{line}'")
                print(f"Reason: {e}")

    return total_cost

# 使用 portfolio3.dat 文件调用函数
if __name__ == '__main__':
    cost = portfolio_cost('/home/labex/project/portfolio3.dat')
    print(cost)
```

在这个更新后的代码中，我们首先打开文件并逐行读取。对于每一行，我们将其拆分为多个字段。然后，我们尝试将股数转换为整数，将价格转换为浮点数。如果这个转换失败（即发生 `ValueError`），我们打印一条警告消息并跳过该行。否则，我们计算这些股票的成本并将其添加到总成本中。

## 测试更新后的函数

现在，让我们使用有问题的文件运行更新后的程序。首先，我们需要导航到项目目录，然后运行 Python 脚本。

```bash
cd /home/labex/project
python3 pcost.py
```

你应该会看到如下输出：

```
Couldn't parse: 'C - 53.08
'
Reason: invalid literal for int() with base 10: '-'
Couldn't parse: 'DIS - 34.20
'
Reason: invalid literal for int() with base 10: '-'
44671.15
```

现在，程序会执行以下操作：

1. 尝试处理文件的每一行。
2. 如果某行包含无效数据，捕获 `ValueError`。
3. 打印有关问题的有用消息。
4. 继续处理文件的其余部分。
5. 根据有效行返回总成本。

这种方法使我们的程序在处理不完美的数据时更加健壮。它可以优雅地处理错误并仍然提供有用的结果。
