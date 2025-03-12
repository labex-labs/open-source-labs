# 理解列格式化问题

在这一步中，我们将探究当前表格格式化实现中的一个局限性。我们还将研究针对此问题的一些可能解决方案。

首先，让我们明确要做什么。我们将打开 VSCode 编辑器，查看项目目录中的 `tableformat.py` 文件。这个文件很重要，因为它包含的代码能让我们以不同方式格式化表格数据，比如文本、CSV 或 HTML 格式。

要打开该文件，我们将在终端中使用以下命令。`cd` 命令用于将目录更改为项目目录，`code` 命令用于在 VSCode 中打开 `tableformat.py` 文件。

```bash
cd ~/project
code tableformat.py
```

当你打开文件时，会注意到定义了几个类。这些类在格式化表格数据方面发挥着不同的作用。

- `TableFormatter`：这是一个抽象基类（abstract base class）。它包含用于格式化表格标题和行的方法。可以将其视为其他格式化器类的蓝图。
- `TextTableFormatter`：此类用于以纯文本格式输出表格。
- `CSVTableFormatter`：它负责将表格数据格式化为 CSV（逗号分隔值，Comma-Separated Values）格式。
- `HTMLTableFormatter`：此类将表格数据格式化为 HTML 格式。

文件中还有一个 `print_table()` 函数。该函数使用我们刚刚提到的格式化器类来显示表格数据。

现在，让我们通过运行一些 Python 代码来看看这些类是如何工作的。打开一个终端并启动 Python 会话。以下代码从 `tableformat.py` 文件中导入必要的函数和类，创建一个 `TextTableFormatter` 对象，然后使用 `print_table()` 函数显示投资组合数据。

```python
python3 -c "
from tableformat import print_table, TextTableFormatter, portfolio
formatter = TextTableFormatter()
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

运行代码后，你应该会看到类似以下的输出：

```
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

现在，让我们找出问题所在。注意，`price` 列中的值格式不一致。有些值有一位小数，如 32.2，而有些值有两位小数，如 51.23。在金融数据中，我们通常希望格式保持一致。

我们期望的输出如下：

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

解决这个问题的一种方法是修改 `print_table()` 函数，使其接受格式规范。以下代码展示了我们如何实现这一点。我们定义了一个新的 `print_table()` 函数，它接受一个额外的 `formats` 参数。在函数内部，我们使用这些格式规范来格式化行中的每个值。

```python
python3 -c "
from tableformat import TextTableFormatter, portfolio

def print_table(records, fields, formats, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [(fmt % getattr(r, fieldname))
             for fieldname, fmt in zip(fields, formats)]
        formatter.row(rowdata)

formatter = TextTableFormatter()
print_table(portfolio,
            ['name','shares','price'],
            ['%s','%d','%0.2f'],
            formatter)
"
```

这个解决方案可行，但有一个缺点。更改函数的接口可能会破坏使用旧版本 `print_table()` 函数的现有代码。

另一种方法是通过子类化创建自定义格式化器。我们可以创建一个继承自 `TextTableFormatter` 的新类，并覆盖 `row()` 方法以应用所需的格式。

```python
python3 -c "
from tableformat import TextTableFormatter, print_table, portfolio

class PortfolioFormatter(TextTableFormatter):
    def row(self, rowdata):
        formats = ['%s','%d','%0.2f']
        rowdata = [(fmt % d) for fmt, d in zip(formats, rowdata)]
        super().row(rowdata)

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

这个解决方案也可行，但不太方便。每次需要不同的格式时，我们都必须创建一个新类。而且我们仅限于从特定的格式化器类型进行子类化，在这种情况下是 `TextTableFormatter`。

在下一步中，我们将探索一种使用混入类（mixin classes）的更优雅的解决方案。
