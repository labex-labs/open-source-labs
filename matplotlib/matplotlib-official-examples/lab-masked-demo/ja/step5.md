# NaN に設定する

y > 0.7 の箇所を NaN に設定します。NaN 値を持つ新しい y 配列を作成します。

```python
y4 = y.copy()
y4[y3 > 0.7] = np.nan
```
