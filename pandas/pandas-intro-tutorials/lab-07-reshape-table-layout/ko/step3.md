# Long 형식에서 Wide 형식 테이블로 변환

이제 `pivot` 함수를 사용하여 대기 질의 long 형식 데이터를 wide 형식으로 변환합니다.

```python
# no2 데이터만 필터링
no2 = air_quality[air_quality["parameter"] == "no2"]

# 각 위치에 대해 2 개의 측정값 사용 (head) (groupby)
no2_subset = no2.sort_index().groupby(["location"]).head(2)

# 데이터 피벗
no2_subset.pivot(columns="location", values="value")
```
