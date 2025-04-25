# マンデルブロ集合関数を定義する

次に、マンデルブロ集合を生成する関数を定義します。この関数にはいくつかのパラメータが必要です。

- `xmin`, `xmax`, `ymin`, `ymax`：x 軸と y 軸の最小値と最大値
- `xn` と `yn`：各軸に沿って生成する点の数
- `maxiter`：各点に対して実行する最大反復回数
- `horizon`：集合の一部と見なす点の最大値

```python
def mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon=2.0):
    X = np.linspace(xmin, xmax, xn).astype(np.float32)
    Y = np.linspace(ymin, ymax, yn).astype(np.float32)
    C = X + Y[:, None] * 1j
    N = np.zeros_like(C, dtype=int)
    Z = np.zeros_like(C)
    for n in range(maxiter):
        I = abs(Z) < horizon
        N[I] = n
        Z[I] = Z[I]**2 + C[I]
    N[N == maxiter-1] = 0
    return Z, N
```
