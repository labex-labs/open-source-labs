# 시계열 데이터 리샘플링 (Resample)

`resample` 메서드는 시계열 데이터의 빈도를 변경하는 강력한 방법입니다. 여기서는 현재 시간별 시계열 데이터를 각 측정 스테이션의 월별 최대값으로 집계합니다.

```python
# By pivoting the data, the datetime information became the index of the table.
no_2 = air_quality.pivot(index="datetime", columns="location", values="value")
no_2.head()

# Create a plot of the values in the different stations from the 20th of May till the end of 21st of May
no_2["2019-05-20":"2019-05-21"].plot()

# resample time series data
monthly_max = no_2.resample("M").max()
monthly_max
```
