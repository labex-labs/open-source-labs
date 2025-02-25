# Построим график средних значений NO2 для каждого часа дня

Мы также можем построить график средних значений NO2 для каждого часа дня. Это можно сделать с использованием метода `plot`.

```python
# plot the average NO2 values for each hour of the day
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel("Hour of the day")
plt.ylabel("$NO_2 (µg/m^3)$")
```
