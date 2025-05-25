# Definir a função para plotar a distribuição beta

Nesta etapa, definimos a função para plotar a distribuição beta.

```python
def plot_beta_hist(ax, a, b):
    ax.hist(np.random.beta(a, b, size=10000),
            histtype="stepfilled", bins=25, alpha=0.8, density=True)
```
