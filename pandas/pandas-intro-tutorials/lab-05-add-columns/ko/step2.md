# 새로운 열 생성

"station_london" 열에 변환 계수를 곱하여 새로운 열 "london_mg_per_cubic"을 생성합니다.

```python
# Create new column by multiplying "station_london" by conversion factor
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
```
