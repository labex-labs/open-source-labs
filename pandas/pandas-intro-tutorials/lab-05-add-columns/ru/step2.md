# Создание новой колонки

Мы создадим новую колонку "london_mg_per_cubic", умножив колонку "station_london" на коэффициент преобразования.

```python
# Create new column by multiplying "station_london" by conversion factor
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
```
