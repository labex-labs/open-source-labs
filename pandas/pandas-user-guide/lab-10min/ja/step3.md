# データフレームの作成

numpy 配列を渡すことで、日付時間インデックスと列名付きの `DataFrame` を作成できます。

```python
# pandas のデータフレームを作成
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df
```
