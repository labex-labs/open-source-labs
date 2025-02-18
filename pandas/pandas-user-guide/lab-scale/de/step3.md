# Effiziente Datentypen verwenden

Die Standard-Datentypen von pandas sind nicht die speicherplatzeffizientesten. Dieser Schritt zeigt, wie man effizientere Datentypen verwendet, um größere Datensätze im Speicher zu speichern.

```python
ts = make_timeseries(freq="30S", seed=0)
ts.to_parquet("timeseries.parquet")
ts = pd.read_parquet("timeseries.parquet")

# Spalte 'name' in den Typ 'category' umwandeln, um Effizienz zu erhöhen
ts2 = ts.copy()
ts2["name"] = ts2["name"].astype("category")

# Numerische Spalten in die kleinsten möglichen Typen umwandeln
ts2["id"] = pd.to_numeric(ts2["id"], downcast="unsigned")
ts2[["x", "y"]] = ts2[["x", "y"]].apply(pd.to_numeric, downcast="float")
```
