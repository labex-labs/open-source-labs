# Criar Normalização de Lei de Potência

Nesta etapa, você precisa criar uma normalização de lei de potência usando `PowerNorm()`.

```python
plt.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```
