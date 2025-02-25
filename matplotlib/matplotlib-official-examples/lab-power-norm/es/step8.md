# Crear normalización por ley de potencia

En este paso, debe crear la normalización por ley de potencia con diferentes valores de gamma.

```python
for ax, gamma in zip(axs.flat[1:], gammas):
    ax.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```
