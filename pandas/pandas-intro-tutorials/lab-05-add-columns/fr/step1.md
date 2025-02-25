# Import Pandas et charger les données

Tout d'abord, nous allons importer la bibliothèque pandas et charger les données de qualité de l'air à partir d'un fichier CSV.

```python
# Import pandas library
import pandas as pd

# Load air quality data
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
```
