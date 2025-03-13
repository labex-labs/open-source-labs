# 使用动态导入

在编程中，导入语句用于从其他模块引入代码，以便我们可以使用它们的功能。然而，有时在文件中间放置导入语句会使代码显得有些杂乱，难以理解。在这部分内容中，我们将学习如何使用动态导入来解决这个问题。动态导入是一项强大的功能，它允许我们在运行时加载模块，这意味着我们仅在实际需要某个模块时才加载它。

首先，我们需要移除当前位于 `TableFormatter` 类之后的导入语句。这些导入属于静态导入，会在程序启动时加载。要完成此操作，请在 WebIDE 中打开 `tableformat/formatter.py` 文件。打开文件后，找到并删除以下几行代码：

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

如果你现在尝试在终端中执行以下命令来运行程序：

```bash
python3 stock.py
```

程序将会运行失败。原因在于格式化器不会被注册到 `_formats` 字典中。你会看到一条关于未知格式的错误消息。这是因为程序无法找到正常运行所需的格式化器类。

为了解决这个问题，我们将修改 `create_formatter` 函数。目标是在需要时动态导入所需的模块。按如下所示更新该函数：

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    if name not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{name}')

    formatter_cls = TableFormatter._formats.get(name)
    if not formatter_cls:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

此函数中最重要的一行代码是：

```python
__import__(f'{__package__}.formats.{name}')
```

这行代码根据格式名称动态导入模块。当模块被导入时，其 `TableFormatter` 的子类会自动进行自我注册。这要归功于我们之前添加的 `__init_subclass__` 方法。该方法是 Python 的一个特殊方法，在创建子类时会被调用，在我们的代码中，它用于注册格式化器类。

完成这些修改后，保存文件。然后，使用以下命令再次运行程序：

```bash
python3 stock.py
```

现在，即使我们移除了静态导入，程序也应该能正常运行。为了验证动态导入是否按预期工作，我们将清空 `_formats` 字典，然后调用 `create_formatter` 函数。在终端中运行以下命令：

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter, create_formatter; TableFormatter._formats.clear(); print('Before:', TableFormatter._formats); create_formatter('text'); print('After:', TableFormatter._formats)"
```

你应该会看到类似如下的输出：

```
Before: {}
After: {'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>}
```

这个输出证实了动态导入在需要时会加载模块并注册格式化器类。

通过使用动态导入和类注册，我们创建了一个更简洁、更易于维护的代码结构。以下是这样做的好处：

1. 现在所有的导入语句都位于文件顶部，这符合 Python 的编程规范。这使得代码更易于阅读和理解。
2. 我们消除了循环导入的问题。循环导入可能会导致程序出现诸如无限循环或难以调试的错误等问题。
3. 代码更加灵活。现在，我们可以添加新的格式化器，而无需修改 `create_formatter` 函数。在实际场景中，随着时间的推移可能会添加新功能，这种方式非常实用。

这种使用动态导入和类注册的模式在插件系统和框架中经常被使用。在这些系统中，组件需要根据用户的需求或程序的要求进行动态加载。
