# Using a Package

A package serves as a namespace for imports.

This means that there are now multilevel imports.

```python
import porty.report
port = porty.report.read_portfolio('portfolio.csv')
```

There are other variations of import statements.

```python
from porty import report
port = report.read_portfolio('portfolio.csv')

from porty.report import read_portfolio
port = read_portfolio('portfolio.csv')
```
