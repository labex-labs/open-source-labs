# 欠損値を補完する

DataFrame 内の欠損値を埋めるために `interpolate` 関数を使用します。

```python
df = pd.DataFrame(
   {
       "A": [1, 2.1, np.nan, 4.7, 5.6, 6.8],
       "B": [0.25, np.nan, np.nan, 4, 12.2, 14.4],
   }
)
df.interpolate()
```
