# Importez les bibliothèques nécessaires et chargez les données

Tout d'abord, nous devons importer les bibliothèques Python requises et charger les données de qualité de l'air. Les données seront lues dans un DataFrame pandas, qui est une structure de données étiquetée en 2 dimensions.

```python
# import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# load the air quality data
air_quality = pd.read_csv("data/air_quality_no2_long.csv")

# rename the "date.utc" column to "datetime"
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
```
