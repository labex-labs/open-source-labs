# Crear normalización por ley de potencia

En este paso, debe crear la normalización por ley de potencia utilizando `PowerNorm()`.

```python
plt.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```
