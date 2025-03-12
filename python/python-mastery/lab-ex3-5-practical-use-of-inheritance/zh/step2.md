# 创建基类并修改打印函数

在编程中，继承是一个强大的概念，它允许我们创建类的层次结构。为了开始使用继承以不同格式输出数据，我们首先需要创建一个基类。基类作为其他类的蓝图，定义了一组通用的方法，其子类可以继承和重写这些方法。

现在，让我们创建一个基类，为所有表格格式化器定义接口。在 WebIDE 中打开 `tableformat.py` 文件，并在文件顶部添加以下代码：

```python
class TableFormatter:
    """
    Base class for all table formatters.
    This class defines the interface that all formatters must implement.
    """
    def headings(self, headers):
        """
        Generate the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Generate a single row of table data.
        """
        raise NotImplementedError()
```

`TableFormatter` 类是一个抽象基类。抽象基类是定义了方法但不提供其实现的类。相反，它期望其子类提供这些实现。`NotImplementedError` 异常用于表明这些方法必须由子类重写。如果子类没有重写这些方法，而我们尝试使用它们，就会引发错误。

接下来，我们需要修改 `print_table()` 函数以使用 `TableFormatter` 类。`print_table()` 函数用于从对象列表中打印数据表格。通过修改它以使用 `TableFormatter` 类，我们可以使该函数更加灵活，能够处理不同的表格格式。

将现有的 `print_table()` 函数替换为以下代码：

```python
def print_table(records, fields, formatter):
    """
    Print a table of data from a list of objects using the specified formatter.

    Args:
        records: A list of objects
        fields: A list of field names
        formatter: A TableFormatter object
    """
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
```

这里的关键变化是 `print_table()` 现在接受一个 `formatter` 参数，该参数应该是 `TableFormatter` 类或其子类的实例。这意味着我们可以将不同的表格格式化器传递给 `print_table()` 函数，它将使用适当的格式化器来打印表格。该函数通过调用格式化器对象的 `headings()` 和 `row()` 方法，将格式化的职责委托给了该对象。

让我们通过尝试使用基类 `TableFormatter` 来测试我们的更改：

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

当你运行这段代码时，你应该会看到一个错误：

```
Traceback (most recent call last):
...
NotImplementedError
```

这个错误的出现是因为我们试图直接使用抽象基类，而它没有为其方法提供实现。由于 `TableFormatter` 类中的 `headings()` 和 `row()` 方法引发了 `NotImplementedError`，当调用这些方法时，Python 不知道该怎么做。在下一步中，我们将创建一个具体的子类来提供这些实现。
