# Archivos `__init__.py`

El propósito principal de estos archivos es unir los módulos.

Ejemplo: consolidando funciones

```python
# porty/__init__.py
from.pcost import portfolio_cost
from.report import portfolio_report
```

Esto hace que los nombres aparezcan en el _nivel superior_ al importar.

```python
from porty import portfolio_cost
portfolio_cost('portfolio.csv')
```

En lugar de usar importaciones de múltiples niveles.

```python
from porty import pcost
pcost.portfolio_cost('portfolio.csv')
```
