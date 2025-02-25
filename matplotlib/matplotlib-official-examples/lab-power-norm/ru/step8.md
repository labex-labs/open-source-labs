# Создание нормализации по степенному закону

В этом шаге вам нужно создать нормализацию по степенному закону с разными значениями gamma.

```python
for ax, gamma in zip(axs.flat[1:], gammas):
    ax.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```
