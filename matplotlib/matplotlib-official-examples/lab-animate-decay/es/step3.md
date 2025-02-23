# Configurar la trama

Ahora, necesitamos configurar la trama. Crearemos una figura y un objeto de ejes utilizando la función `subplots()` de Matplotlib. También crearemos un objeto de línea para representar la onda senoidal.

```python
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []
```
