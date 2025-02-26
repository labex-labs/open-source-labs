# Using a Package

Un package sert de nommage pour les importations.

Cela signifie qu'il existe désormais des importations multi-niveaux.

```python
import porty.report
port = porty.report.read_portfolio('portfolio.csv')
```

Il existe d'autres variantes d'instructions d'importation.

```python
from porty import report
port = report.read_portfolio('portfolio.csv')

from porty.report import read_portfolio
port = read_portfolio('portfolio.csv')
```
