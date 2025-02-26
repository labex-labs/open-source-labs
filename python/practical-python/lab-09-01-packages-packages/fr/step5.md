# Problem: Imports

Les importations entre fichiers dans le même package _doivent désormais inclure le nom du package dans l'import_. Rappelez-vous la structure.

```code
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

Exemple d'import modifié.

```python
from porty import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

Toutes les importations sont _absolues_, pas relatives.

```python
import fileparse    # NE FONCTIONNE PAS. fileparse non trouvé

...
```
