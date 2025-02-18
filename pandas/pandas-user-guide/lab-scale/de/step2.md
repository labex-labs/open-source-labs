# Weniger Daten laden

Anstatt alle Daten zu laden, können wir nur die Spalten laden, die wir benötigen. Hier demonstrieren wir zwei Methoden, um weniger Daten aus der Parquet-Datei zu laden.

```python
# Option 1: Alle Daten laden und dann filtern
columns = ["id_0", "name_0", "x_0", "y_0"]
pd.read_parquet("timeseries_wide.parquet")[columns]

# Option 2: Nur die angeforderten Spalten laden
pd.read_parquet("timeseries_wide.parquet", columns=columns)
```
