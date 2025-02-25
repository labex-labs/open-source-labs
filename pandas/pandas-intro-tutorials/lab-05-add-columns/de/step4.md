# Spaltenbezeichnungen umbenennen

Wir werden die Spaltenbezeichnungen umbenennen, um den von OpenAQ verwendeten Stationenbezeichnern zu entsprechen.

```python
# Rename column labels
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)
```
