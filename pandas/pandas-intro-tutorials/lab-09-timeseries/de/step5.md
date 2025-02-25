# Zeichnen der durchschnittlichen NO2-Werte für jede Stunde des Tages

Wir können auch die durchschnittlichen NO2-Werte für jede Stunde des Tages plotten. Dies kann mit der `plot`-Methode durchgeführt werden.

```python
# plot the average NO2 values for each hour of the day
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel("Hour of the day")
plt.ylabel("$NO_2 (µg/m^3)$")
```
