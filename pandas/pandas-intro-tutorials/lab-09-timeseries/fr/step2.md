# Convertir des chaînes de caractères en objets datetime

Les dates dans la colonne "datetime" sont actuellement des chaînes de caractères. Nous voulons les convertir en objets datetime pour une manipulation plus facile.

```python
# convert "datetime" column to datetime objects
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])
```
