# 1 日の各時間における平均 NO2 値をプロットする

1 日の各時間における平均 NO2 値をプロットすることもできます。これは、`plot` メソッドを使って行うことができます。

```python
# 1 日の各時間における平均 NO2 値をプロットする
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel("Hour of the day")
plt.ylabel("$NO_2 (µg/m^3)$")
```
