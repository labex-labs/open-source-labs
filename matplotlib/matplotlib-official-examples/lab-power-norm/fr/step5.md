# Créer une normalisation par loi de puissance

Dans cette étape, vous devez créer une normalisation par loi de puissance à l'aide de `PowerNorm()`.

```python
plt.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```
