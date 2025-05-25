# 요일별 평균 NO2 농도 계산

이제 각 측정 위치에서 요일별 평균 NO2 농도를 계산할 수 있습니다. 이는 `groupby` 메서드를 사용하여 수행할 수 있습니다.

```python
# calculate the average NO2 concentration for each day of the week
average_NO2 = air_quality.groupby([air_quality["datetime"].dt.weekday, "location"])["value"].mean()
```
