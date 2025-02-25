# 2 つの列の値の比率を確認する

次に、「station_paris」と「station_antwerp」の列の値の比率を確認し、その結果を新しい列に保存します。

```python
# Create new column by dividing "station_paris" by "station_antwerp"
air_quality["ratio_paris_antwerp"] = air_quality["station_paris"] / air_quality["station_antwerp"]
```
