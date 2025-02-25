# NumPy との違いを理解する

Pandas と NumPy は、分散を計算する方法に若干の違いがあります。この 2 つのライブラリ間で切り替える際に考慮することが重要です。

```python
# Variance in pandas
var_pandas = df.var()

# Variance in NumPy
var_numpy = np.var(df.values)
```
