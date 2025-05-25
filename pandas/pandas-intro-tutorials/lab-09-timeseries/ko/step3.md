# 측정 월에 대한 새로운 열 추가

이제 각 측정의 월만 포함하는 새로운 열을 DataFrame 에 추가하려고 합니다. 이는 `dt` 접근자를 사용하여 수행할 수 있습니다.

```python
# add a new column for the month of each measurement
air_quality["month"] = air_quality["datetime"].dt.month
```
