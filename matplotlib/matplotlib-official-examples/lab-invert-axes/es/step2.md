# Crear datos

A continuación, necesitamos crear algunos datos para graficar. En este ejemplo, crearemos una matriz de valores para el tiempo (`t`) y una matriz de valores para la tensión (`s`).

```python
t = np.arange(0.01, 5.0, 0.01)
s = np.exp(-t)
```
