# Переименовать метки колонок

Мы переименуем метки колонок, чтобы они соответствовали идентификаторам станций, используемым OpenAQ.

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
