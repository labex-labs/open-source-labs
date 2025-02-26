# Fichiers `__init__.py`

Le principal but de ces fichiers est de rassembler les modules.

Exemple : consolidation de fonctions

```python
# porty/__init__.py
from.pcost import portfolio_cost
from.report import portfolio_report
```

Cela permet d'avoir les noms disponibles au _niveau supérieur_ lors de l'importation.

```python
from porty import portfolio_cost
portfolio_cost('portfolio.csv')
```

Plutôt que d'utiliser des importations multi-niveaux.

```python
from porty import pcost
pcost.portfolio_cost('portfolio.csv')
```
