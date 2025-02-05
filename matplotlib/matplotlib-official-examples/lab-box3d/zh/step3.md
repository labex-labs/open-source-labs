# 绘制等高面

使用 `contourf` 方法为盒子的每个表面绘制等高面。为 `zdir` 和 `offset` 使用适当的参数。

```python
kw = {
    'vmin': data.min(),
    'vmax': data.max(),
    'levels': np.linspace(data.min(), data.max(), 10),
}

# 创建一个带有 3D 轴的图形
fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(111, projection='3d')

# 绘制等高面
_ = ax.contourf(
    X[:, :, 0], Y[:, :, 0], data[:, :, 0],
    zdir='z', offset=0, **kw
)
_ = ax.contourf(
    X[0, :, :], data[0, :, :], Z[0, :, :],
    zdir='y', offset=0, **kw
)
C = ax.contourf(
    data[:, -1, :], Y[:, -1, :], Z[:, -1, :],
    zdir='x', offset=X.max(), **kw
)
```
