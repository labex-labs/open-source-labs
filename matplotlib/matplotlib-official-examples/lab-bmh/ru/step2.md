# Определяем функцию для построения бета-распределения

В этом шаге мы определяем функцию для построения бета-распределения.

```python
def plot_beta_hist(ax, a, b):
    ax.hist(np.random.beta(a, b, size=10000),
            histtype="stepfilled", bins=25, alpha=0.8, density=True)
```
