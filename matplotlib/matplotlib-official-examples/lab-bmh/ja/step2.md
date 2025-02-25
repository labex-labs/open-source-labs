# ベータ分布を描画する関数を定義する

このステップでは、ベータ分布を描画する関数を定義します。

```python
def plot_beta_hist(ax, a, b):
    ax.hist(np.random.beta(a, b, size=10000),
            histtype="stepfilled", bins=25, alpha=0.8, density=True)
```
