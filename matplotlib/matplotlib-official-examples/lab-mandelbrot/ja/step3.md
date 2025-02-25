# マンデルブロ集合を生成する

次に、必要なパラメータを使って `mandelbrot_set` 関数を呼び出して、マンデルブロ集合を生成します。これにより、2つの配列が得られます。

- `Z`：反復処理した複素数の最終値
- `N`：各点が集合の一部と判定されるまでに実行した反復回数

```python
xmin, xmax, xn = -2.25, +0.75, 3000 // 2
ymin, ymax, yn = -1.25, +1.25, 2500 // 2
maxiter = 200
horizon = 2.0 ** 40
log_horizon = np.log2(np.log(horizon))
Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)
```
