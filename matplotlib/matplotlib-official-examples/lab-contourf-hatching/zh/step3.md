# 带颜色条的最简单阴影图

在这一步中，我们将创建一个带颜色条的最简单阴影图。我们将使用 `contourf` 函数来创建填充等高线图，并使用 `hatches` 参数指定阴影图案。

```python
fig1, ax1 = plt.subplots()
cs = ax1.contourf(x, y, z, hatches=['-', '/', '\\', '//'],
                  cmap='gray', extend='both', alpha=0.5)
fig1.colorbar(cs)
```
