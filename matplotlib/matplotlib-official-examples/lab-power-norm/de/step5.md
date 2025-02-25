# Potenzgesetz-Normalisierung erstellen

In diesem Schritt müssen Sie die Potenzgesetz-Normalisierung mithilfe von `PowerNorm()` erstellen.

```python
plt.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```
