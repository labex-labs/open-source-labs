# 列ラベルをリネームする

OpenAQ が使用する測定所識別子に一致するように、列ラベルをリネームします。

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
