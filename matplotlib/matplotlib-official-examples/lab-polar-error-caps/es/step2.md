# Crear datos

En este paso, crearemos los datos para nuestro gráfico de barras de error. Utilizaremos NumPy para crear una matriz de valores de theta y una matriz de valores de radio correspondientes.

```python
theta = np.arange(0, 2 * np.pi, np.pi / 4)
r = theta / np.pi / 2 + 0.5
```
