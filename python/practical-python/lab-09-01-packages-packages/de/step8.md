# `__init__.py`-Dateien

Der primäre Zweck dieser Dateien besteht darin, Module zusammenzusetzen.

Beispiel: Zusammenführen von Funktionen

```python
# porty/__init__.py
from.pcost import portfolio_cost
from.report import portfolio_report
```

Dadurch erscheinen die Namen auf der _Hauptebene_, wenn importiert wird.

```python
from porty import portfolio_cost
portfolio_cost('portfolio.csv')
```

Anstatt die mehrstufigen Imports zu verwenden.

```python
from porty import pcost
pcost.portfolio_cost('portfolio.csv')
```
