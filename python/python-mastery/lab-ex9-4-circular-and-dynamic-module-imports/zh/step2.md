# 探究循环导入

循环导入是指两个或多个模块相互依赖的情况。具体来说，当模块 A 导入模块 B，而模块 B 也直接或间接地导入模块 A 时，就会出现这种情况。这会形成一个依赖循环，Python 的导入系统无法正确解决这个问题。简单来说，Python 在尝试确定先导入哪个模块时会陷入循环，这可能会导致程序出错。

让我们通过代码实验来看看循环导入会如何引发问题。

首先，我们将运行股票程序，检查它在当前结构下是否能正常工作。这一步有助于我们建立一个基准，在进行任何更改之前，了解程序按预期运行的情况。

```bash
cd ~/project/structly
python3 stock.py
```

程序应该能正确运行，并以格式化表格的形式显示股票数据。如果可以正常运行，这意味着当前的代码结构没有循环导入问题，运行良好。

现在，我们要修改 `formatter.py` 文件。通常，将导入语句移到文件顶部是一个好的做法。这样可以使代码更有条理，一眼就能看懂。

```bash
cd ~/project/structly
```

在 WebIDE 中打开 `tableformat/formatter.py` 文件。我们将把以下导入语句移到文件顶部，放在现有导入语句之后。这些导入语句是针对不同的表格格式化器的，如文本、CSV 和 HTML 格式。

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

现在，文件开头应该如下所示：

```python
# formatter.py
from abc import ABC, abstractmethod
from .mixins import ColumnFormatMixin, UpperHeadersMixin
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

保存文件，然后再次尝试运行股票程序。

```bash
python3 stock.py
```

你应该会看到一条关于 `TableFormatter` 未定义的错误消息。这是循环导入问题的明显迹象。

问题的产生是由于以下一系列事件：

1. `formatter.py` 尝试从 `formats/text.py` 导入 `TextTableFormatter`。
2. `formats/text.py` 从 `formatter.py` 导入 `TableFormatter`。
3. 当 Python 尝试解析这些导入时，它会陷入循环，因为它无法决定先完全导入哪个模块。

让我们撤销更改，使程序再次正常工作。编辑 `tableformat/formatter.py` 文件，将导入语句移回原来的位置（在 `TableFormatter` 类定义之后）。

```python
# formatter.py
from abc import ABC, abstractmethod
from .mixins import ColumnFormatMixin, UpperHeadersMixin

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

再次运行程序，确认它能正常工作。

```bash
python3 stock.py
```

这表明，尽管从代码组织的角度来看，将导入语句放在文件中间不是最佳做法，但这样做是为了避免循环导入问题。在接下来的步骤中，我们将探索更好的解决方案。
