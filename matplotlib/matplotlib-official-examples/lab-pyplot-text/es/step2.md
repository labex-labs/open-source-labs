# Crear datos

A continuación, crearemos los datos para el gráfico. Crearemos una onda senoidal utilizando la biblioteca `numpy`.

```python
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)
```
