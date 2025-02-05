# 定义绘制贝塔分布的函数

在这一步中，我们定义绘制贝塔分布的函数。

```python
def plot_beta_hist(ax, a, b):
    ax.hist(np.random.beta(a, b, size=10000),
            histtype="stepfilled", bins=25, alpha=0.8, density=True)
```
