# Объединение таблиц с использованием общего идентификатора

Затем мы добавим координаты станций в таблицу измерений с использованием функции `merge`. Мы выполним левый внешний join по столбцу `location`.

```python
# Load the stations coordinates data
stations_coord = pd.read_csv("data/air_quality_stations.csv")

# Merge the air_quality and stations_coord dataframes
air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
```
