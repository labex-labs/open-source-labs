# 循环导入

尝试将以下导入语句移动到 `formatter.py` 文件的顶部：

```python
# formatter.py

from.formats.text import TextTableFormatter
from.formats.csv import CSVTableFormatter
from.formats.html import HTMLTableFormatter

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

...
```

注意，现在一切都无法正常工作了。尝试运行 `stock.py` 程序，并注意到关于未定义 `TableFormatter` 的错误。导入语句的顺序很重要，你不能随意将导入语句移动到任何你想要的位置。

把导入语句移回原来的位置。唉。
