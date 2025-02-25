# データを生成する

`numpy` ライブラリを使って、指数関数的減衰関数 `np.exp(-t / 5.0)` のデータを生成します。

```python
dt = 0.01
t = np.arange(dt, 20.0, dt)
```
