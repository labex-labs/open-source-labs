# Agregar ruido a los datos

En este paso, agregaremos algo de ruido a los datos para que se vean más realistas. Usaremos la función `normal` de NumPy para generar números aleatorios con una media de 0,0 y una desviación estándar de 0,3.

```python
# Add noise to the data
nse = np.random.normal(0.0, 0.3, t.shape) * s
```
