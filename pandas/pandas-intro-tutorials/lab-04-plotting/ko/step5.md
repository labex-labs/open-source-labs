# 산점도 생성

런던과 파리에서 측정된 NO2 값을 시각적으로 비교하기 위해 산점도 (scatter plot) 를 생성할 수 있습니다.

```python
# Creating a scatter plot
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()
```
