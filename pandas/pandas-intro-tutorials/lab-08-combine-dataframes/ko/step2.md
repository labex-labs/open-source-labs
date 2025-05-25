# 데이터 세트 로드

대기 질과 관련된 두 개의 데이터 세트를 로드합니다. 하나는 질산염 데이터를 포함하고 다른 하나는 미세 입자 물질 데이터를 포함합니다.

```python
# Load the Nitrate data
air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv", parse_dates=True)
air_quality_no2 = air_quality_no2[["date.utc", "location", "parameter", "value"]]

# Load the Particulate matter data
air_quality_pm25 = pd.read_csv("data/air_quality_pm25_long.csv", parse_dates=True)
air_quality_pm25 = air_quality_pm25[["date.utc", "location", "parameter", "value"]]
```
