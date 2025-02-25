# Überprüfen des Verhältnisses von Werten in zwei Spalten

Als nächstes überprüfen wir das Verhältnis der Werte in den Spalten "station_paris" und "station_antwerp" und speichern das Ergebnis in einer neuen Spalte.

```python
# Create new column by dividing "station_paris" by "station_antwerp"
air_quality["ratio_paris_antwerp"] = air_quality["station_paris"] / air_quality["station_antwerp"]
```
