# 新しい列を作成する

「station_london」列に換算係数を掛けることで、新しい列「london_mg_per_cubic」を作成します。

```python
# Create new column by multiplying "station_london" by conversion factor
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
```
