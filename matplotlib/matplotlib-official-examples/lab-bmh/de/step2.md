# Definieren der Funktion zum Zeichnen der Beta-Verteilung

In diesem Schritt definieren wir die Funktion zum Zeichnen der Beta-Verteilung.

```python
def plot_beta_hist(ax, a, b):
    ax.hist(np.random.beta(a, b, size=10000),
            histtype="stepfilled", bins=25, alpha=0.8, density=True)
```
