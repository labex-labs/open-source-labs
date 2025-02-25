# Creando la señal

Crearemos una señal utilizando NumPy. Crearemos una matriz `xdata` utilizando la función `linspace` con `start = 16`, `stop = 365` y `num = (365 - 16)*4`. Crearemos una matriz `ydata` utilizando las funciones `sin` y `cos`.

```python
xdata = np.linspace(16, 365, (365-16)*4)
ydata = np.sin(2*np.pi*xdata/153) + np.cos(2*np.pi*xdata/127)
```
