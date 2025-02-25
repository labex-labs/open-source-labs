# Importation des bibliothèques et chargement des données

Tout d'abord, importons les bibliothèques requises et chargeons les jeux de données.

```python
import pandas as pd

# Charger le jeu de données Titanic
titanic = pd.read_csv("data/titanic.csv")

# Charger le jeu de données Air Quality
air_quality = pd.read_csv("data/air_quality_long.csv", index_col="date.utc", parse_dates=True)
```
