# 欠損値を検出する

次に、欠損値を検出するために `isna` 関数と `notna` 関数を使用します。

```python
# 欠損値を検出するために isna と notna を使用する
pd.isna(df2["one"])
df2["four"].notna()
df2.isna()
```
