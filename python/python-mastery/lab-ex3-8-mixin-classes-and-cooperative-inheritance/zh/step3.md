# 为混入类创建用户友好的 API

混入类是 Python 中强大的特性，但对于初学者来说可能有点棘手，因为它涉及多重继承，这可能会变得相当复杂。在这一步中，我们将通过改进 `create_formatter()` 函数，让用户使用起来更加轻松。这样，用户就不必过多担心多重继承的细节。

首先，你需要打开 `tableformat.py` 文件。你可以在终端中运行以下命令来完成此操作。`cd` 命令用于将目录更改为你的项目文件夹，`code` 命令用于在代码编辑器中打开 `tableformat.py` 文件。

```bash
cd ~/project
code tableformat.py
```

文件打开后，找到 `create_formatter()` 函数。目前，它的代码如下：

```python
def create_formatter(name):
    """
    Create an appropriate formatter based on the name.
    """
    if name == 'text':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')
```

这个函数接受一个名称作为参数，并返回相应的格式化器。但我们希望让它更灵活。我们将对其进行修改，使其能够接受混入类的可选参数。

将现有的 `create_formatter()` 函数替换为下面增强后的版本。这个新函数允许你指定列格式以及是否将标题转换为大写。

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    """
    Create a formatter with optional enhancements.

    Parameters:
    name : str
        Name of the formatter ('text', 'csv', 'html')
    column_formats : list, optional
        List of format strings for column formatting
    upper_headers : bool, optional
        Whether to convert headers to uppercase
    """
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {name}')

    # Apply mixins if requested
    if column_formats and upper_headers:
        class CustomFormatter(ColumnFormatMixin, UpperHeadersMixin, formatter_cls):
            formats = column_formats
        return CustomFormatter()
    elif column_formats:
        class CustomFormatter(ColumnFormatMixin, formatter_cls):
            formats = column_formats
        return CustomFormatter()
    elif upper_headers:
        class CustomFormatter(UpperHeadersMixin, formatter_cls):
            pass
        return CustomFormatter()
    else:
        return formatter_cls()
```

这个增强后的函数首先根据 `name` 参数确定基本的格式化器类。然后，根据是否提供了 `column_formats` 和 `upper_headers`，创建一个包含适当混入类的自定义格式化器类。最后，返回自定义格式化器类的一个实例。

现在，让我们使用不同的选项组合来测试这个增强后的函数。

首先，让我们尝试使用列格式化。在终端中运行以下命令。这个命令从 `tableformat.py` 文件中导入必要的函数和数据，创建一个带有列格式化的格式化器，然后使用该格式化器打印一个表格。

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', column_formats=['%s', '%d', '%0.2f'])
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

你应该会看到列已格式化的表格。输出如下：

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

接下来，让我们尝试使用大写标题。运行以下命令：

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', upper_headers=True)
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

你应该会看到带有大写标题的表格。输出如下：

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

最后，让我们将两个选项结合起来。运行以下命令：

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', column_formats=['%s', '%d', '%0.2f'], upper_headers=True)
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

这应该会显示一个列已格式化且标题为大写的表格。输出如下：

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

这个增强后的函数也适用于其他类型的格式化器。例如，让我们尝试使用 CSV 格式化器。运行以下命令：

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('csv', column_formats=['\\"%s\\"', '%d', '%0.2f'])
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

这应该会生成列已格式化的 CSV 输出。输出如下：

```
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
```

通过增强 `create_formatter()` 函数，我们创建了一个用户友好的 API。现在，用户可以轻松使用混入类，而不必了解多重继承的复杂细节。这让他们能够根据自己的需求灵活定制格式化器。
