# `__init__.py` 文件

这些文件的主要目的是将模块组合在一起。

示例：整合函数

```python
# porty/__init__.py
from.pcost import portfolio_cost
from.report import portfolio_report
```

这使得在导入时，名称出现在**顶级**。

```python
from porty import portfolio_cost
portfolio_cost('portfolio.csv')
```

而不是使用多级导入。

```python
from porty import pcost
pcost.portfolio_cost('portfolio.csv')
```
