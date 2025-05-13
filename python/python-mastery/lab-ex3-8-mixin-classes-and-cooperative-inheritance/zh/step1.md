# 理解列格式化的问题

在这一步中，我们将研究当前表格格式化实现中的一个局限性。我们还将检查一些解决此问题的可能方案。

首先，让我们了解我们将要做什么。我们将打开 VSCode 编辑器，并查看项目目录中的 `tableformat.py` 文件。这个文件非常重要，因为它包含允许我们以不同方式格式化表格数据的代码，例如文本、CSV 或 HTML 格式。

要打开该文件，我们将在终端中使用以下命令。`cd` 命令将目录更改为项目目录，`code` 命令在 VSCode 中打开 `tableformat.py` 文件。

```bash
cd ~/project
touch tableformat.py
```

当你打开文件时，你会注意到定义了几个类。这些类在格式化表格数据中扮演着不同的角色。

- `TableFormatter`：这是一个抽象基类（abstract base class）。它具有用于格式化表头和行的方法。可以将其视为其他格式化器类的蓝图。
- `TextTableFormatter`：此类用于以纯文本格式输出表格。
- `CSVTableFormatter`：它负责以 CSV（逗号分隔值）格式格式化表格数据。
- `HTMLTableFormatter`：此类以 HTML 格式格式化表格数据。

文件中还有一个 `print_table()` 函数。此函数使用我们刚刚提到的格式化器类来显示表格数据。

现在，让我们看看这些类是如何工作的。在你的 `/home/labex/project` 目录中，使用你的编辑器或 `touch` 命令创建一个名为 `step1_test1.py` 的新文件。将以下 Python 代码添加到其中：

```python
# step1_test1.py
from tableformat import print_table, TextTableFormatter, portfolio

formatter = TextTableFormatter()
print("--- Running Step 1 Test 1 ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-----------------------------")
```

保存文件并在终端中运行它：

```bash
python3 step1_test1.py
```

运行脚本后，你应该看到类似于以下的输出：

```
--- Running Step 1 Test 1 ---
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
-----------------------------
```

现在，让我们找到问题。请注意，`price` 列中的值未以一致的方式格式化。有些值有一位小数，例如 32.2，而另一些值有两位小数，例如 51.23。在财务数据中，我们通常希望格式化保持一致。

这是我们希望输出的样子：

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

一种解决方法是修改 `print_table()` 函数以接受格式规范。让我们看看这是如何工作的，*而不*实际修改 `tableformat.py`。创建一个名为 `step1_test2.py` 的新文件，其内容如下。此脚本在本地重新定义 `print_table` 函数以进行演示。

```python
# step1_test2.py
from tableformat import TextTableFormatter

# Re-define Stock and portfolio locally for this example
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

portfolio = [
    Stock('AA', 100, 32.20), Stock('IBM', 50, 91.10), Stock('CAT', 150, 83.44),
    Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.10),
    Stock('IBM', 100, 70.44)
]

# Define a modified print_table locally
def print_table_modified(records, fields, formats, formatter):
    formatter.headings(fields)
    for r in records:
        # Apply formats to the original attribute values
        rowdata = [(fmt % getattr(r, fieldname))
                   for fieldname, fmt in zip(fields, formats)]
        # Pass the already formatted strings to the formatter's row method
        formatter.row(rowdata)

print("--- Running Step 1 Test 2 ---")
formatter = TextTableFormatter()
# Note: TextTableFormatter.row expects strings already formatted for width.
# This example might not align perfectly yet, but demonstrates passing formats.
print_table_modified(portfolio,
                     ['name', 'shares', 'price'],
                     ['%10s', '%10d', '%10.2f'], # Using widths
                     formatter)
print("-----------------------------")

```

运行此脚本：

```bash
python3 step1_test2.py
```

这种方法演示了传递格式，但是修改 `print_table` 有一个缺点：更改函数的接口可能会破坏使用原始版本的现有代码。

另一种方法是通过子类化（subclassing）创建自定义格式化器。我们可以创建一个新类，该类继承自 `TextTableFormatter` 并覆盖（override） `row()` 方法。创建一个文件 `step1_test3.py`：

```python
# step1_test3.py
from tableformat import TextTableFormatter, print_table, portfolio

class PortfolioFormatter(TextTableFormatter):
    def row(self, rowdata):
        # Example: Add a prefix to demonstrate overriding
        # Note: The original lab description's formatting example had data type issues
        # because print_table sends strings to this method. This is a simpler demo.
        print("> ", end="") # Add a simple prefix to the line start
        super().row(rowdata) # Call the parent method

print("--- Running Step 1 Test 3 ---")
formatter = PortfolioFormatter()
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-----------------------------")
```

运行脚本：

```bash
python3 step1_test3.py
```

此解决方案适用于演示子类化，但是为每个格式化变体创建一个新类并不方便。此外，你还受限于你继承的基类（这里是 `TextTableFormatter`）。

在下一步中，我们将探索使用 mixin 类的一种更优雅的解决方案。
