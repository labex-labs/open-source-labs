# Generar datos

Generamos algunos datos de muestra para graficar. Aquí, usamos la biblioteca `numpy` para generar tres arrays de datos.

```python
t = np.arange(0.0, 2.0, 0.01)

s1 = np.sin(2 * np.pi * t)
s2 = np.exp(-t)
s3 = s1 * s2
```
