# 文字列メソッドを使用する

Pandas は、文字列データを操作しやすくする一連の文字列処理メソッドを提供しています。これらのメソッドは、欠損値/NA 値を自動的に除外します。

```python
s = pd.Series(
    ["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"], dtype="string"
)

# 小文字に変換する
s.str.lower()

# 大文字に変換する
s.str.upper()

# 各文字列の長さを計算する
s.str.len()
```
