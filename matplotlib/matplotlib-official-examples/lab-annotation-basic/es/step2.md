# Crear una gráfica

A continuación, crearemos una gráfica utilizando Matplotlib. En este ejemplo, graficaremos la función coseno en un rango de valores.

```python
fig, ax = plt.subplots()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)
```
