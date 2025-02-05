# 创建对数刻度的图表

我们重复上一步，但这次使用对数刻度。我们注意到，对数刻度会导致基于整数的子采样在标记距离上产生视觉上的不对称，而基于分数的子采样则会产生均匀分布。

```python
# 创建对数刻度的图表
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```
