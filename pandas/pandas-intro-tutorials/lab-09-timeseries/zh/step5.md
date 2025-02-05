# 绘制一天中每小时的平均二氧化氮值

我们还可以绘制一天中每小时的平均二氧化氮值。这可以使用 `plot` 方法来完成。

```python
# 绘制一天中每小时的平均二氧化氮值
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel("Hour of the day")
plt.ylabel("$NO_2 (µg/m^3)$")
```
