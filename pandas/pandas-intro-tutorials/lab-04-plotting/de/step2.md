# Laden der Daten

Wir werden für diesen Tutorial Luftqualitätsdaten verwenden. Die Daten werden aus einer CSV-Datei in einen Pandas DataFrame geladen.

```python
# Loading the data
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
air_quality.head()
```
