# 공통 식별자를 사용하여 테이블 병합 (Merge Tables Using a Common Identifier)

그런 다음 `merge` 함수를 사용하여 측정 테이블에 스테이션 좌표를 추가합니다. `location` 열을 기준으로 왼쪽 조인 (left join) 을 수행합니다.

```python
# Load the stations coordinates data
stations_coord = pd.read_csv("data/air_quality_stations.csv")

# Merge the air_quality and stations_coord dataframes
air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
```
