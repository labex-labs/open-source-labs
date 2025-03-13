# 理解导入问题

让我们先了解一下什么是模块导入。在 Python 中，当你想使用另一个文件（模块）中的函数、类或变量时，你会使用 `import` 语句。然而，导入的结构方式可能会导致各种问题。

现在，我们来研究一个有问题的模块结构示例。`tableformat/formatter.py` 中的代码，其导入语句分散在整个文件中。乍一看，这似乎不是什么大问题，但它会带来维护和依赖方面的问题。

首先，打开 WebIDE 文件浏览器，导航到 `structly` 目录。我们将运行几个命令来了解项目的当前结构。`cd` 命令用于更改当前工作目录，`ls -la` 命令用于列出当前目录中的所有文件和目录，包括隐藏文件。

```bash
cd ~/project/structly
ls -la
```

这将显示项目目录中的文件。现在，我们使用 `cat` 命令查看其中一个有问题的文件，该命令用于显示文件的内容。

```bash
cat tableformat/formatter.py
```

你应该会看到类似于以下的代码：

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

def create_formatter(name, column_formats=None, upper_headers=False):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

注意导入语句位于文件中间。这存在几个问题：

1. 这使得代码更难阅读和维护。当你查看一个文件时，你期望在开头看到所有的导入语句，这样你就能快速了解该文件依赖哪些外部模块。
2. 这可能会导致循环导入问题。当两个或多个模块相互依赖时，就会发生循环导入，这可能会导致错误，并使你的代码行为异常。
3. 这违反了 Python 将所有导入语句放在文件顶部的约定。遵循约定可以使你的代码更易读，也更便于其他开发者理解。

在接下来的步骤中，我们将更详细地探讨这些问题，并学习如何解决它们。
