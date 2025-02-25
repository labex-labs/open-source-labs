# データを読み込む

このチュートリアルでは、空気質データを使用します。このデータは CSV ファイルから Pandas の DataFrame に読み込まれます。

```python
# Loading the data
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
air_quality.head()
```
