# 创建线性刻度的图表

接下来，我们创建一组子图，以展示 `markevery` 在线性刻度下的表现。我们遍历 `cases` 列表，并在单独的子图上绘制每个情况。我们使用 `markevery` 参数来指定要标记哪些数据点。

```python
# 创建线性刻度的图表
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```
