# Créer une normalisation par loi de puissance

Dans cette étape, vous devez créer une normalisation par loi de puissance avec différentes valeurs de gamma.

```python
for ax, gamma in zip(axs.flat[1:], gammas):
    ax.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```
