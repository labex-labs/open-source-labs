# Creando la gráfica

Crearemos una gráfica utilizando Matplotlib. Crearemos una instancia `d` de la clase `DataDisplayDownsampler` utilizando `xdata` e `ydata`. Crearemos una figura y un eje utilizando la función `subplots`. Conectaremos la línea y estableceremos la autoscala en `False`. Conectaremos para cambiar los límites de vista, estableceremos el límite `x` y mostraremos la gráfica.

```python
d = DataDisplayDownsampler(xdata, ydata)
fig, ax = plt.subplots()
d.line, = ax.plot(xdata, ydata, 'o-')
ax.set_autoscale_on(False)
ax.callbacks.connect('xlim_changed', d.update)
ax.set_xlim(16, 365)
plt.show()
```
