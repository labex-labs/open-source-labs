# Преобразуем строки в объекты datetime

Даты в столбце "datetime" в настоящее время представлены в виде строк. Мы хотим преобразовать их в объекты datetime для более удобной обработки.

```python
# convert "datetime" column to datetime objects
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])
```
