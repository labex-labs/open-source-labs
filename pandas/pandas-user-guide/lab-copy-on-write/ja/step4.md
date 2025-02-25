# Copy-On-Write を使ったチェーンド代入の実装

最後に、`loc` メソッドを使って Copy-On-Write を伴うチェーンド代入をどのように実装するか見てみましょう。

```python
# DataFrame を作成
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# 'loc' を使って Copy-On-Write を伴うチェーンド代入を適用
df.loc[df["bar"] > 5, "foo"] = 100

# DataFrame を表示
print(df)
```
