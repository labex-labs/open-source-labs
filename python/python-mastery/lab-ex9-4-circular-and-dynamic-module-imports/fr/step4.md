# Importations dynamiques

Vous êtes maintenant prêt pour la dernière étape. Supprimez complètement les instructions d'importation suivantes :

```python
# formatter.py
...

from.formats.text import TextTableFormatter     # DELETE
from.formats.csv import CSVTableFormatter       # DELETE
from.formats.html import HTMLTableFormatter     # DELETE
...
```

Exécutez à nouveau votre code `stock.py` - il devrait échouer avec une erreur. Il ne connaît rien du formateur de texte. Corrigez-le en ajoutant ce fragment de code à `create_formatter()` :

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    if name not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{name}')
  ...
```

Ce code tente une importation dynamique d'un module de formateur si rien n'est connu du nom. L'importation seule (si elle fonctionne) enregistrera la classe dans le dictionnaire `_formats` et tout fonctionnera. Magie!

Essayez d'exécuter le code `stock.py` et assurez-vous qu'il fonctionne ensuite.
