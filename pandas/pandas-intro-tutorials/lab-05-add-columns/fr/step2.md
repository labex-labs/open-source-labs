# Créer une nouvelle colonne

Nous allons créer une nouvelle colonne, "london_mg_per_cubic", en multipliant la colonne "station_london" par un facteur de conversion.

```python
# Create new column by multiplying "station_london" by conversion factor
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
```
