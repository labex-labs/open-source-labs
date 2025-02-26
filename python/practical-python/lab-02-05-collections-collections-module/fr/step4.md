# Exemple : Conserver une historique

Problème : Nous voulons une historique des N derniers éléments. Solution : Utiliser un `deque`.

```python
from collections import deque

history = deque(maxlen=N)
with open(filename) as f:
    for line in f:
        history.append(line)
     ...
```

Le module `collections` est peut-être l'un des modules de bibliothèque les plus utiles pour traiter des problèmes de manipulation de données à usage spécifique tels que le tabulation et l'indexation.

Dans cet exercice, nous allons examiner quelques exemples simples. Commencez par exécuter votre programme `report.py` pour charger le portefeuille d'actions en mode interactif.

```bash
$ python3 -i report.py
```
