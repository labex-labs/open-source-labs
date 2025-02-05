# `__init__.py` files

The primary purpose of these files is to stitch modules together.

Example: consolidating functions

```python
# porty/__init__.py
from .pcost import portfolio_cost
from .report import portfolio_report
```

This makes names appear at the _top-level_ when importing.

```python
from porty import portfolio_cost
portfolio_cost('portfolio.csv')
```

Instead of using the multilevel imports.

```python
from porty import pcost
pcost.portfolio_cost('portfolio.csv')
```
