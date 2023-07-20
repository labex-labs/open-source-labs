# Plot the average NO2 values for each hour of the day

We can also plot the average NO2 values for each hour of the day. This can be done using the `plot` method.

```python
# plot the average NO2 values for each hour of the day
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel("Hour of the day")
plt.ylabel("$NO_2 (µg/m^3)$")
```
