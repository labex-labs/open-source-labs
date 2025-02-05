# 创建幂律归一化

在这一步中，你需要使用不同的伽马值创建幂律归一化。

```python
for ax, gamma in zip(axs.flat[1:], gammas):
    ax.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```
