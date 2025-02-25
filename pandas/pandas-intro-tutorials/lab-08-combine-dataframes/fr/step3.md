# Concaténer les ensembles de données

Ensuite, nous allons combiner les mesures de nitrates et de matières particulaires dans un seul tableau à l'aide de la fonction `concat`.

```python
# Concatenate the two dataframes
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
```
