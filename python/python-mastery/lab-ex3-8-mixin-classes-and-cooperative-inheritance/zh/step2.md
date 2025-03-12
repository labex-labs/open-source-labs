# 实现用于格式化的混入类

在这一步中，你将学习混入类（mixin classes）。混入类是 Python 中非常实用的技术。它能让你在不改变类原有代码的情况下，为类添加额外的功能。这很棒，因为它有助于保持代码的模块化，便于管理。

## 什么是混入类？

混入类是一种特殊类型的类。其主要目的是提供一些可以被其他类继承的功能。不过，混入类并非单独使用。你不会直接创建混入类的实例。相反，你可以用它以一种可控且可预测的方式为其他类添加特定功能。这是多重继承（multiple inheritance）的一种形式，即一个类可以从多个父类继承。

现在，让我们在 `tableformat.py` 文件中实现两个混入类。首先，在编辑器中打开该文件。你可以在终端中运行以下命令来完成此操作：

```bash
cd ~/project
code tableformat.py
```

文件打开后，在文件末尾、现有函数之前添加以下类定义：

```python
class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)
```

这个 `ColumnFormatMixin` 类提供列格式化功能。`formats` 类变量是一个列表，用于存储格式代码。这些代码用于格式化每列的数据。`row()` 方法接收行数据，将格式代码应用于行中的每个元素，然后使用 `super().row(rowdata)` 将格式化后的行数据传递给父类。

接下来，添加另一个混入类，使表格标题以大写形式显示：

```python
class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])
```

这个 `UpperHeadersMixin` 类将标题文本转换为大写。它接收标题列表，将每个标题转换为大写，然后使用 `super().headings()` 将修改后的标题传递给父类的 `headings()` 方法。

## 使用混入类

让我们测试一下新的混入类。运行一些 Python 代码，看看它们是如何工作的。

```python
python3 -c "
from tableformat import TextTableFormatter, ColumnFormatMixin, portfolio, print_table

class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

运行此代码时，你应该会看到格式良好的输出。由于 `ColumnFormatMixin` 提供的格式化功能，价格列将具有一致的小数位数。

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

现在，让我们尝试使用 `UpperHeadersMixin`。运行以下代码：

```python
python3 -c "
from tableformat import TextTableFormatter, UpperHeadersMixin, portfolio, print_table

class PortfolioFormatter(UpperHeadersMixin, TextTableFormatter):
    pass

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

此代码应将标题显示为大写。

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

## 理解协作式继承

注意，在混入类中，我们使用了 `super().method()`。这被称为“协作式继承（cooperative inheritance）”。在协作式继承中，继承链中的每个类都协同工作。当一个类调用 `super().method()` 时，它是在请求链中的下一个类执行其任务。这样，一系列类可以各自为整个过程添加自己的行为。

继承顺序非常重要。当我们定义 `class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter)` 时，Python 首先在 `ColumnFormatMixin` 中查找方法，然后在 `TextTableFormatter` 中查找。因此，当在 `ColumnFormatMixin` 中调用 `super().row()` 时，它指的是 `TextTableFormatter.row()`。

我们甚至可以将两个混入类结合使用。运行以下代码：

```python
python3 -c "
from tableformat import TextTableFormatter, ColumnFormatMixin, UpperHeadersMixin, portfolio, print_table

class PortfolioFormatter(ColumnFormatMixin, UpperHeadersMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']

formatter = PortfolioFormatter()
print_table(portfolio, ['name','shares','price'], formatter)
"
```

此代码将同时显示大写标题和格式化后的数字。

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

在下一步中，我们将通过增强 `create_formatter()` 函数，让这些混入类更易于使用。
