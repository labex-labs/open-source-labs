# Plotar os valores médios de NO2 para cada hora do dia

Também podemos plotar os valores médios de NO2 para cada hora do dia. Isso pode ser feito usando o método `plot`.

```python
# plot the average NO2 values for each hour of the day
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel("Hour of the day")
plt.ylabel("$NO_2 (µg/m^3)$")
```
