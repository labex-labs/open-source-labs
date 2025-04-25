# nullable 整数配列を使った演算

nullable 整数配列を使って、算術演算、比較、スライシングなど、様々な演算を行うことができます。

```python
# nullable 整数型の Series を作成
s = pd.Series([1, 2, None], dtype="Int64")

# 算術演算を行う
s_plus_one = s + 1 # Series の各要素に 1 を加える

# 比較を行う
comparison = s == 1 # Series の各要素が 1 と等しいかどうかを確認する

# スライシング演算を行う
sliced = s.iloc[1:3] # Series の 2 番目と 3 番目の要素を選択する
```
