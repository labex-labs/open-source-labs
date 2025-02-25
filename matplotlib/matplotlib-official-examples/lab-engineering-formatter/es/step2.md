# Crear datos artificiales

Necesitamos crear algunos datos artificiales para graficar. En este laboratorio, graficaremos el logaritmo de la frecuencia (en Hz) contra el logaritmo de la potencia (en Watts). Usaremos la biblioteca `numpy` para generar los datos.

```python
# Fixing random state for reproducibility
prng = np.random.RandomState(19680801)

# Create artificial data to plot.
# The x data span over several decades to demonstrate several SI prefixes.
xs = np.logspace(1, 9, 100)
ys = (0.8 + 0.4 * prng.uniform(size=100)) * np.log10(xs)**2
```
