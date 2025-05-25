# Arquivos `__init__.py`

O objetivo principal desses arquivos é unir módulos.

Exemplo: consolidando funções

```python
# porty/__init__.py
from .pcost import portfolio_cost
from .report import portfolio_report
```

Isso faz com que os nomes apareçam no _nível superior_ (top-level) ao importar.

```python
from porty import portfolio_cost
portfolio_cost('portfolio.csv')
```

Em vez de usar os imports de múltiplos níveis.

```python
from porty import pcost
pcost.portfolio_cost('portfolio.csv')
```
