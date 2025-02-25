# データを正規化する

マンデルブロ集合の陰影付きで電力正規化されたレンダリングを作成するために、データを正規化する必要があります。これは、以下の式を使って行います。

`M = N + 1 - np.log2(np.log(abs(Z))) + log_horizon`

```python
with np.errstate(invalid='ignore'):
    M = np.nan_to_num(N + 1 - np.log2(np.log(abs(Z))) + log_horizon)
```
