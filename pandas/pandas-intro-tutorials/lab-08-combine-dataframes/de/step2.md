# Lade die Datensätze

Wir werden zwei Datensätze zu Luftqualität laden. Einer enthält Nitratdaten und der andere enthält Feinstaubdaten.

```python
# Load the Nitrate data
air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv", parse_dates=True)
air_quality_no2 = air_quality_no2[["date.utc", "location", "parameter", "value"]]

# Load the Particulate matter data
air_quality_pm25 = pd.read_csv("data/air_quality_pm25_long.csv", parse_dates=True)
air_quality_pm25 = air_quality_pm25[["date.utc", "location", "parameter", "value"]]
```
