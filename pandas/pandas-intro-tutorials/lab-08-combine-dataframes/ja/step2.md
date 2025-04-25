# データセットを読み込む

私たちは、空気質に関連する 2 つのデータセットを読み込みます。1 つは硝酸塩データを含み、もう 1 つは微粒子状物質データを含みます。

```python
# 硝酸塩データを読み込む
air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv", parse_dates=True)
air_quality_no2 = air_quality_no2[["date.utc", "location", "parameter", "value"]]

# 微粒子状物質データを読み込む
air_quality_pm25 = pd.read_csv("data/air_quality_pm25_long.csv", parse_dates=True)
air_quality_pm25 = air_quality_pm25[["date.utc", "location", "parameter", "value"]]
```
