# 長形式のデータを幅広のテーブル形式に変換する

ここでは、`pivot` 関数を使用して、大気質の長形式のデータを幅広の形式に変換します。

```python
# no2 データのみを抽出する
no2 = air_quality[air_quality["parameter"] == "no2"]

# 各場所（groupby）に対して 2 つの測定値（head）を使用する
no2_subset = no2.sort_index().groupby(["location"]).head(2)

# データをピボットする
no2_subset.pivot(columns="location", values="value")
```
