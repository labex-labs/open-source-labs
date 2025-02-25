# Добавляем новый столбец с месяцем измерения

Теперь мы хотим добавить новый столбец в наш DataFrame, содержащий только месяц каждого измерения. Это можно сделать с использованием доступатора `dt`.

```python
# add a new column for the month of each measurement
air_quality["month"] = air_quality["datetime"].dt.month
```
