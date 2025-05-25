# 매개변수의 전체 설명 및 이름 추가 (Add Parameters' Full Description and Name)

마지막으로, 측정 테이블에 매개변수의 전체 설명과 이름을 추가합니다. `parameter` 및 `id` 열을 기준으로 왼쪽 조인 (left join) 을 수행합니다.

```python
# Load the air quality parameters data
air_quality_parameters = pd.read_csv("data/air_quality_parameters.csv")

# Merge the air_quality and air_quality_parameters dataframes
air_quality = pd.merge(air_quality, air_quality_parameters, how='left', left_on='parameter', right_on='id')
```
