# 하루의 각 시간대별 평균 NO2 값 플롯

또한 하루의 각 시간대별 평균 NO2 값을 플롯할 수 있습니다. 이는 `plot` 메서드를 사용하여 수행할 수 있습니다.

```python
# plot the average NO2 values for each hour of the day
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel("Hour of the day")
plt.ylabel("$NO_2 (µg/m^3)$")
```
