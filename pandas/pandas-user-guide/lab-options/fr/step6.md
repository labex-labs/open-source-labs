# Définir les options de démarrage

Nous pouvons créer un script de démarrage dans l'environnement Python/IPython pour importer pandas et définir des options, ce qui rend le travail avec pandas plus efficace.

```python
# Voici un exemple de script de démarrage
# Placez-le dans un fichier.py dans le répertoire de démarrage du profil IPython
import pandas as pd

pd.set_option("display.max_rows", 999)
pd.set_option("display.precision", 5)
```
