# 幅広の形式を長形式に変換する

次に、`melt` 関数を使って、幅広の形式の 𝑁𝑂2 データを長形式に変換しましょう。

```python
# no2_pivoted のインデックスをリセットする
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()

# データをメルトする
no_2 = no2_pivoted.melt(id_vars="date.utc")
```
