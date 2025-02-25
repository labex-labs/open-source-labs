# DataFrame を使った Copy-On-Write の理解

では、DataFrame を作成して、CoW がデータの変更にどのように影響するか見てみましょう。

```python
# DataFrame を作成
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# DataFrame のサブセットを作成
subset = df["foo"]

# サブセットを変更
subset.iloc[0] = 100

# 元の DataFrame を表示
print(df)
```

## DataFrame で Copy-On-Write を実装する

では、DataFrame を変更する際に CoW をどのように実装するか見てみましょう。

```python
# CoW を有効にする
pd.options.mode.copy_on_write = True

# DataFrame のサブセットを作成
subset = df["foo"]

# サブセットを変更
subset.iloc[0] = 100

# 元の DataFrame を表示
print(df)
```
