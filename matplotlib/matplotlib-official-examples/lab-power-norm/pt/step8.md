# Criar Normalização de Lei de Potência

Nesta etapa, você precisa criar uma normalização de lei de potência com diferentes valores de gama (gamma).

```python
for ax, gamma in zip(axs.flat[1:], gammas):
    ax.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```
