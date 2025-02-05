# 设置标题

在这一步中，你需要为每个图表设置标题。

```python
axs[0, 0].set_title('线性归一化')

for ax, gamma in zip(axs.flat[1:], gammas):
    ax.set_title(r'幂律 ($\gamma = %1.1f$)' % gamma)
```
