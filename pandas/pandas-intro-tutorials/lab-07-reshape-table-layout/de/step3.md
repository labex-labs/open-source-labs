# Umwandlung von langem in breites Tabellenformat

Wir werden nun die langformatigen Luftqualitätsdaten in das breite Format umwandeln, indem wir die `pivot`-Funktion verwenden.

```python
# Filtern Sie nur nach NO2-Daten
no2 = air_quality[air_quality["parameter"] == "no2"]

# Verwenden Sie 2 Messungen (head) für jede Location (groupby)
no2_subset = no2.sort_index().groupby(["location"]).head(2)

# Drehen Sie die Daten
no2_subset.pivot(columns="location", values="value")
```
