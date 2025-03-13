# 实现子类注册

在编程中，循环导入可能是个棘手的问题。我们可以采用注册模式，而非直接导入格式化器类。在这种模式下，子类会向其父类进行自我注册。这是一种常见且有效的避免循环导入的方法。

首先，让我们了解如何获取类的模块名。模块名很重要，因为我们会在注册模式中用到它。为此，我们将在终端中运行一个 Python 命令。

```bash
cd ~/project/structly
python3 -c "from structly.tableformat.formats.text import TextTableFormatter; print(TextTableFormatter.__module__); print(TextTableFormatter.__module__.split('.')[-1])"
```

当你运行这个命令时，会看到如下输出：

```
structly.tableformat.formats.text
text
```

这个输出表明，我们可以从类本身提取模块名。稍后，我们会用这个模块名来注册子类。

现在，让我们修改 `tableformat/formatter.py` 文件中的 `TableFormatter` 类，添加一个注册机制。在 WebIDE 中打开这个文件。我们将在 `TableFormatter` 类中添加一些代码，这些代码将帮助我们自动注册子类。

```python
class TableFormatter(ABC):
    _formats = { }  # Dictionary to store registered formatters

    @classmethod
    def __init_subclass__(cls):
        name = cls.__module__.split('.')[-1]
        TableFormatter._formats[name] = cls

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

`__init_subclass__` 方法是 Python 中的一个特殊方法。每当创建 `TableFormatter` 的子类时，就会调用这个方法。在这个方法中，我们提取子类的模块名，并将其作为键，把该子类注册到 `_formats` 字典中。

接下来，我们需要修改 `create_formatter` 函数，以使用这个注册字典。这个函数负责根据给定的名称创建合适的格式化器。

```python
def create_formatter(name, column_formats=None, upper_headers=False):
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

完成这些修改后，保存文件。然后，让我们测试一下程序是否仍然可以正常运行。我们将运行 `stock.py` 脚本。

```bash
python3 stock.py
```

如果程序能正确运行，就说明我们的修改没有破坏任何功能。现在，让我们查看 `_formats` 字典的内容，看看注册是如何工作的。

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter; print(TableFormatter._formats)"
```

你应该会看到如下输出：

```
{'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>, 'csv': <class 'structly.tableformat.formats.csv.CSVTableFormatter'>, 'html': <class 'structly.tableformat.formats.html.HTMLTableFormatter'>}
```

这个输出证实了我们的子类已正确注册到 `_formats` 字典中。不过，我们的文件中间仍然存在一些导入语句。在下一步中，我们将使用动态导入来解决这个问题。
