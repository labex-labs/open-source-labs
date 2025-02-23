# Amélioration de l'expérience du shell

Pour améliorer l'expérience du shell, créez un module (`shelltools.py`) avec des méthodes d'aide qui peuvent être importées dans la session interactive. Ce module peut contenir des méthodes d'aide supplémentaires pour des tâches telles que l'initialisation de la base de données ou la suppression de tables.

```python
# Fichier : shelltools.py

def initialize_database():
    # Code pour initialiser la base de données
    pass

def drop_tables():
    # Code pour supprimer les tables
    pass
```

Dans le shell interactif, importez les méthodes souhaitées à partir du module `shelltools`.

```python
# Fichier : shell.py
# Exécution : python shell.py

from shelltools import initialize_database, drop_tables

# Importez les méthodes souhaitées à partir du module shelltools
from shelltools import *

# Utilisez les méthodes importées
initialize_database()
drop_tables()
```
