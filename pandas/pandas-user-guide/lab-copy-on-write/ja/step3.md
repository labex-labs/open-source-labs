# Copy-On-Write とチェーンド代入の理解

では、チェーンド代入が CoW とどのように機能するかを理解しましょう。

```python
# DataFrame を作成
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# CoW の原則に違反するチェーンド代入を適用
df["foo"][df["bar"] > 5] = 100

# DataFrame を表示
print(df)
```
