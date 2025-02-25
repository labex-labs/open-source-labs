# Generar datos

Generaremos 100.000 puntos de datos utilizando `numpy.random.standard_normal()` y `numpy.random.standard_normal()`. `standard_normal()` genera números aleatorios a partir de una distribución normal estándar con una media de 0 y una desviación estándar de 1.

```python
np.random.seed(19680801)

n = 100_000
x = np.random.standard_normal(n)
y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)
xlim = x.min(), x.max()
ylim = y.min(), y.max()
```
