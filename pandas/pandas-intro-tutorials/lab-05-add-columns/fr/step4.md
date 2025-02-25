# Renommer les étiquettes de colonnes

Nous allons renommer les étiquettes de colonnes pour correspondre aux identifiants de stations utilisés par OpenAQ.

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
