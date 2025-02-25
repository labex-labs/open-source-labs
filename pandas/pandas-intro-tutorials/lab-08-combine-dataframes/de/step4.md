# Tabellen mithilfe eines gemeinsamen Identifikators zusammenführen

Anschließend werden wir die Standortkoordinaten zur Messungstabelle hinzufügen, indem wir die `merge`-Funktion verwenden. Wir werden einen linken Join auf der `location`-Spalte durchführen.

```python
# Load the stations coordinates data
stations_coord = pd.read_csv("data/air_quality_stations.csv")

# Merge the air_quality and stations_coord dataframes
air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
```
