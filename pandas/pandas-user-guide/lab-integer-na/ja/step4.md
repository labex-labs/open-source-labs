# pandas.NAを使った欠損値の処理

`IntegerArray`クラスは、スカラーの欠損値として`pandas.NA`を使用します。欠損している単一の要素をスライスすると、`pandas.NA`が返されます。

```python
# 欠損値を持つIntegerArrayを作成
a = pd.array([1, None], dtype="Int64")

# 欠損値である2番目の要素をスライスする
missing_value = a[1]
# 出力: <NA>
```
