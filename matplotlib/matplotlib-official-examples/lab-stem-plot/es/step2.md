# Generar datos

A continuación, necesitamos generar algunos datos para utilizar en nuestra gráfica de tallo. Crearemos dos arrays utilizando la biblioteca Numpy.

```python
x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))
```
