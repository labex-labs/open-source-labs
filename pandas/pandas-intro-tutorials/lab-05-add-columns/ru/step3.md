# Проверить отношение значений в двух колонках

Далее мы проверим отношение значений в колонках "station_paris" и "station_antwerp" и сохраним результат в новую колонку.

```python
# Create new column by dividing "station_paris" by "station_antwerp"
air_quality["ratio_paris_antwerp"] = air_quality["station_paris"] / air_quality["station_antwerp"]
```
