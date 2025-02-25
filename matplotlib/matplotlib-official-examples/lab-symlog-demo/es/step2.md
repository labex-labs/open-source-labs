# Generar datos

A continuación, necesitamos generar algunos datos para graficar. En este ejemplo, crearemos tres arrays: uno para los valores del eje x, uno para los valores del eje y en la primera gráfica y uno para los valores del eje y en la tercera gráfica.

```python
dt = 0.01
x = np.arange(-50.0, 50.0, dt)
y1 = np.arange(0, 100.0, dt)
y3 = np.sin(x / 3.0)
```
