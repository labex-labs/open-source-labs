# 使用包

包用作导入的命名空间。

这意味着现在有了多级导入。

```python
import porty.report
port = porty.report.read_portfolio('portfolio.csv')
```

导入语句还有其他变体。

```python
from porty import report
port = report.read_portfolio('portfolio.csv')

from porty.report import read_portfolio
port = read_portfolio('portfolio.csv')
```
