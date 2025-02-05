# 重命名列标签

我们将重命名列标签，使其与 OpenAQ 使用的站点标识符相匹配。

```python
# 重命名列标签
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)
```
