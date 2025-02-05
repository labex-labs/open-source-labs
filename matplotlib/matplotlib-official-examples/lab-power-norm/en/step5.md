# Create Power Law Normalization

In this step, you need to create power law normalization using `PowerNorm()`.

```python
plt.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```
