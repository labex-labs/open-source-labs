# 生成曼德勃罗集

现在我们将通过使用所需参数调用 `mandelbrot_set` 函数来生成曼德勃罗集。这将为我们提供两个数组：

- `Z`：我们迭代的复数的最终值
- `N`：在确定每个点是集合的一部分之前对其执行的迭代次数

```python
xmin, xmax, xn = -2.25, +0.75, 3000 // 2
ymin, ymax, yn = -1.25, +1.25, 2500 // 2
maxiter = 200
horizon = 2.0 ** 40
log_horizon = np.log2(np.log(horizon))
Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)
```
