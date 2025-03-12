# 实现异常处理

在这一步中，我们将着重让你的代码变得更加健壮。当程序遇到无效数据时，通常会崩溃。但我们可以使用一种名为异常处理的技术来优雅地处理这些问题。你将修改 `reader.py` 文件以实现这一点。异常处理能让你的程序即使在遇到意外数据时也能继续运行，而不是突然停止。

## 理解 try-except 块

Python 提供了一种强大的方式来使用 try-except 块处理异常。下面我们来详细了解它们的工作原理。

```python
try:
    # Code that might cause an exception
    result = risky_operation()
except SomeExceptionType as e:
    # Code that runs if the exception occurs
    handle_exception(e)
```

在 `try` 块中，你放置可能引发异常的代码。异常是程序执行过程中出现的错误。例如，如果你尝试将一个数除以零，Python 会引发一个 `ZeroDivisionError` 异常。当 `try` 块中出现异常时，Python 会停止执行 `try` 块中的代码，并跳转到匹配的 `except` 块。`except` 块包含处理异常的代码。`SomeExceptionType` 是你想要捕获的异常类型。你可以捕获特定类型的异常，也可以使用通用的 `Exception` 来捕获所有类型的异常。`as e` 部分允许你访问异常对象，该对象包含有关错误的信息。

## 修改代码

现在，让我们将所学的 try-except 块知识应用到 `convert_csv()` 函数中。在编辑器中打开 `reader.py` 文件。

1. 将当前的 `convert_csv()` 函数替换为以下代码：

```python
def convert_csv(rows, converter, header=True):
    """
    Convert a sequence of rows to an output sequence according to a conversion function.
    """
    if header:
        headers = next(rows)
    else:
        headers = []

    result = []
    for row_idx, row in enumerate(rows, start=1):
        try:
            # Try to convert the row
            result.append(converter(headers, row))
        except Exception as e:
            # Print a warning message for bad rows
            print(f"Row {row_idx}: Bad row: {row}")
            continue

    return result
```

在这个新的实现中：

- 我们使用 `for` 循环而不是 `map()` 来处理每一行。这让我们对每一行的处理有更多的控制权。
- 我们将转换代码包裹在 try-except 块中。这意味着如果在转换某一行时出现异常，程序不会崩溃，而是会跳转到 `except` 块。
- 在 `except` 块中，我们为无效行打印一条错误消息。这有助于我们识别哪些行有问题。
- 打印错误消息后，我们使用 `continue` 语句跳过当前行并继续处理剩余的行。

完成这些更改后保存文件。

## 测试你的更改

让我们使用 `missing.csv` 文件来测试你修改后的代码。首先，在终端中运行以下命令打开 Python 解释器：

```bash
python3
```

进入 Python 解释器后，运行以下代码：

```python
from reader import read_csv_as_dicts
port = read_csv_as_dicts('missing.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(port)}")
```

运行这段代码时，你应该会看到每一个有问题的行的错误消息。但程序会继续处理并返回有效的行。以下是你可能看到的输出示例：

```
Row 4: Bad row: ['C', '', '53.08']
Row 7: Bad row: ['DIS', '50', 'N/A']
Row 8: Bad row: ['GE', '', '37.23']
Row 13: Bad row: ['INTC', '', '21.84']
Row 17: Bad row: ['MCD', '', '51.11']
Row 19: Bad row: ['MO', '', '70.09']
Row 22: Bad row: ['PFE', '', '26.40']
Row 26: Bad row: ['VZ', '', '42.92']
Number of valid rows processed: 20
```

我们还来验证一下程序在处理有效数据时是否能正常工作。在 Python 解释器中运行以下代码：

```python
valid_port = read_csv_as_dicts('valid.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(valid_port)}")
```

你应该会看到所有行都被无错误地处理。以下是输出示例：

```
Number of valid rows processed: 17
```

要退出 Python 解释器，运行以下命令：

```python
exit()
```

现在你的代码更加健壮了。它可以通过跳过无效行来优雅地处理无效数据，而不是崩溃。这使得你的程序更加可靠和用户友好。
