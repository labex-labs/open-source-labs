# 为 `print_table()` 函数添加类型检查

在这一步中，我们将改进 `tableformat.py` 文件中的 `print_table()` 函数。我们会添加一个检查，以确保 `formatter` 参数是一个有效的 `TableFormatter` 实例。为什么需要这样做呢？类型检查就像是代码的安全网，它能确保你处理的数据类型正确，从而避免许多难以发现的错误。

## 理解 Python 中的类型检查

类型检查是编程中非常有用的技术，它能让你在开发过程的早期捕获错误。在 Python 中，我们经常处理不同类型的对象，有时我们期望将特定类型的对象传递给函数。要检查一个对象是否是特定类型或其子类的实例，可以使用 `isinstance()` 函数。例如，如果你有一个期望传入列表的函数，就可以使用 `isinstance()` 来确保输入确实是一个列表。

## 修改 `print_table()` 函数

首先，在代码编辑器中打开 `tableformat.py` 文件。滚动到文件底部，你会找到 `print_table()` 函数。它最初的样子如下：

```python
def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
```

这个函数接受一些数据、列名列表和一个格式化器，然后使用该格式化器打印表格。但目前，它没有检查格式化器的类型是否正确。

让我们修改它以添加类型检查。我们将使用 `isinstance()` 函数来检查 `formatter` 参数是否是 `TableFormatter` 的实例。如果不是，我们将抛出一个带有明确信息的 `TypeError`。修改后的代码如下：

```python
def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")

    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
```

## 测试类型检查的实现

现在我们已经添加了类型检查，需要确保它能正常工作。让我们创建一个名为 `test_tableformat.py` 的新 Python 文件。你应该在其中放入以下代码：

```python
import stock
import reader
import tableformat

# Read portfolio data
portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)

# Define a formatter that doesn't inherit from TableFormatter
class MyFormatter:
    def headings(self, headers):
        pass
    def row(self, rowdata):
        pass

# Try to use the non-compliant formatter
try:
    tableformat.print_table(portfolio, ['name', 'shares', 'price'], MyFormatter())
    print("Test failed - type checking not implemented")
except TypeError as e:
    print(f"Test passed - caught error: {e}")
```

在这段代码中，我们首先读取一些投资组合数据。然后定义一个名为 `MyFormatter` 的新格式化器类，它不继承自 `TableFormatter`。我们尝试在 `print_table()` 函数中使用这个不符合要求的格式化器。如果我们的类型检查正常工作，它应该抛出一个 `TypeError`。

要运行测试，打开终端并导航到 `test_tableformat.py` 文件所在的目录。然后运行以下命令：

```bash
python test_tableformat.py
```

如果一切正常，你应该会看到如下输出：

```
Test passed - caught error: Expected a TableFormatter
```

这个输出确认了我们的类型检查按预期工作。现在，`print_table()` 函数将只接受 `TableFormatter` 实例或其子类的格式化器。
