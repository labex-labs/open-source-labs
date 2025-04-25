# 週の各日における平均 NO2 濃度を計算する

これで、各測定地点における週の各日の平均 NO2 濃度を計算することができます。これは、`groupby` メソッドを使って行うことができます。

```python
# 週の各日における平均 NO2 濃度を計算する
average_NO2 = air_quality.groupby([air_quality["datetime"].dt.weekday, "location"])["value"].mean()
```
