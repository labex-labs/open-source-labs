# 定义曼德勃罗集函数

接下来，我们将定义一个生成曼德勃罗集的函数。该函数接受几个参数：

- `xmin`、`xmax`、`ymin`、`ymax`：x 轴和 y 轴的最小值和最大值
- `xn` 和 `yn`：沿每个轴生成的点数
- `maxiter`：对每个点执行的最大迭代次数
- `horizon`：将一个点视为集合一部分的最大值

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
