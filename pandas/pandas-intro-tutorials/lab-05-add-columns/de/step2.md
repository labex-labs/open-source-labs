# Eine neue Spalte erstellen

Wir werden eine neue Spalte namens "london_mg_per_cubic" erstellen, indem wir die Spalte "station_london" mit einem Umrechnungsfaktor multiplizieren.

```python
# Create new column by multiplying "station_london" by conversion factor
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
```
