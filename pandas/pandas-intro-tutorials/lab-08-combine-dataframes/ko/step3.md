# 데이터 세트 연결 (Concatenating the Datasets)

다음으로, `concat` 함수를 사용하여 질산염과 미세 입자 물질의 측정값을 단일 테이블로 결합합니다.

```python
# Concatenate the two dataframes
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
```
