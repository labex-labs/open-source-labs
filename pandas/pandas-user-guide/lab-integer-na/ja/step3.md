# nullable整数配列を使った演算

nullable整数配列を使って、算術演算、比較、スライシングなど、様々な演算を行うことができます。

```python
# nullable整数型のSeriesを作成
s = pd.Series([1, 2, None], dtype="Int64")

# 算術演算を行う
s_plus_one = s + 1 # Seriesの各要素に1を加える

# 比較を行う
comparison = s == 1 # Seriesの各要素が1と等しいかどうかを確認する

# スライシング演算を行う
sliced = s.iloc[1:3] # Seriesの2番目と3番目の要素を選択する
```
