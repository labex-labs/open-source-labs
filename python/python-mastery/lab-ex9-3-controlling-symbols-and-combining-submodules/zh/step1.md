# 准备工作

包的一个潜在麻烦之处在于它们会使导入语句变得复杂。例如，在 `stock.py` 程序中，你现在有如下的导入语句：

```python
from structly.structure import Structure
from structly.reader import read_csv_as_instances
from structly.tableformat import create_formatter, print_table
```

如果这个包打算作为一个统一的整体来使用，那么将所有内容整合到一个顶级包中可能会更合理（也更简单）。我们来这么做：
