# Create Power Law Normalization

In this step, you need to create power law normalization with different gamma values.

```python
for ax, gamma in zip(axs.flat[1:], gammas):
    ax.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```
