# Potenzgesetz-Normalisierung erstellen

In diesem Schritt müssen Sie die Potenzgesetz-Normalisierung mit unterschiedlichen Gamma-Werten erstellen.

```python
for ax, gamma in zip(axs.flat[1:], gammas):
    ax.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```
