# Crear datos para los gráficos

Necesitamos crear datos para los gráficos que se visualizarán. En este ejemplo, crearemos tres conjuntos de datos diferentes utilizando NumPy.

```python
t = np.arange(0.01, 5.0, 0.01)
s1 = np.sin(2 * np.pi * t)
s2 = np.exp(-t)
s3 = np.sin(4 * np.pi * t)
```
