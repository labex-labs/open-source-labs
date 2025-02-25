# Definir la función para trazar la distribución beta

En este paso, definimos la función para trazar la distribución beta.

```python
def plot_beta_hist(ax, a, b):
    ax.hist(np.random.beta(a, b, size=10000),
            histtype="stepfilled", bins=25, alpha=0.8, density=True)
```
