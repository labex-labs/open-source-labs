# Vérifier le ratio des valeurs dans deux colonnes

Ensuite, nous allons vérifier le ratio des valeurs dans les colonnes "station_paris" et "station_antwerp" et enregistrer le résultat dans une nouvelle colonne.

```python
# Create new column by dividing "station_paris" by "station_antwerp"
air_quality["ratio_paris_antwerp"] = air_quality["station_paris"] / air_quality["station_antwerp"]
```
