# Graficar los valores promedio de NO2 para cada hora del día

También podemos graficar los valores promedio de NO2 para cada hora del día. Esto se puede hacer utilizando el método `plot`.

```python
# plot the average NO2 values for each hour of the day
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel("Hour of the day")
plt.ylabel("$NO_2 (µg/m^3)$")
```
