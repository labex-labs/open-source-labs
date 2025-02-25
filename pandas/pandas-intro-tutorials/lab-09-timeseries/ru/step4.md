# Вычисляем среднюю концентрацию NO2 для каждого дня недели

Теперь мы можем вычислить среднюю концентрацию NO2 для каждого дня недели в каждом месте измерения. Это можно сделать с использованием метода `groupby`.

```python
# calculate the average NO2 concentration for each day of the week
average_NO2 = air_quality.groupby([air_quality["datetime"].dt.weekday, "location"])["value"].mean()
```
