# 데이터 로드

이 튜토리얼에서는 대기 질 데이터를 사용합니다. 데이터는 CSV 파일에서 Pandas DataFrame 으로 로드됩니다.

```python
# Loading the data
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
air_quality.head()
```
