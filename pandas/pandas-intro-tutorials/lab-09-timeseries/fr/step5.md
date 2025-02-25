# Tracez les valeurs moyennes de NO2 pour chaque heure de la journée

Nous pouvons également tracer les valeurs moyennes de NO2 pour chaque heure de la journée. Cela peut être fait à l'aide de la méthode `plot`.

```python
# plot the average NO2 values for each hour of the day
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel("Hour of the day")
plt.ylabel("$NO_2 (µg/m^3)$")
```
