# Importation de l'ensemble de données

La première étape consiste à importer l'ensemble de données que nous allons utiliser.

```python
# Importation de la bibliothèque pandas
import pandas as pd

# Lecture de l'ensemble de données
titanic = pd.read_csv("data/titanic.csv")

# Affichage des cinq premières lignes de l'ensemble de données
titanic.head()
```
