# Umwandlung von breitem in langes Format

Nun wandeln wir die breitformatigen Daten von 𝑁𝑂2 in das langformat mit der `melt`-Funktion um.

```python
# Setzen Sie den Index für no2_pivoted zurück
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()

# Schmelzen Sie die Daten
no_2 = no2_pivoted.melt(id_vars="date.utc")
```
