# 두 열의 값 비율 확인

다음으로, "station_paris" 및 "station_antwerp" 열의 값 비율을 확인하고 결과를 새로운 열에 저장합니다.

```python
# Create new column by dividing "station_paris" by "station_antwerp"
air_quality["ratio_paris_antwerp"] = air_quality["station_paris"] / air_quality["station_antwerp"]
```
