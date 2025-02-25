# Définissez la fonction pour tracer la distribution bêta

Dans cette étape, nous définissons la fonction pour tracer la distribution bêta.

```python
def plot_beta_hist(ax, a, b):
    ax.hist(np.random.beta(a, b, size=10000),
            histtype="stepfilled", bins=25, alpha=0.8, density=True)
```
