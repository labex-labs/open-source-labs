# 创建缩放图

我们创建另一组子图，这次是为了展示 `markevery` 在缩放图上的表现。我们注意到，基于整数的子采样从基础数据中选择点，并且与视图无关，而基于浮点数的子采样与轴对角线相关，并会改变显示的数据范围。

```python
# 创建缩放图
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
    ax.set_xlim((6, 6.7))
    ax.set_ylim((1.1, 1.7))
```
