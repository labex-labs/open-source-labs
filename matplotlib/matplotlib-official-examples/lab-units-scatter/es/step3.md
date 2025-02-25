# Crear gráficos

En este paso, crearemos tres gráficos utilizando la matriz enmascarada con diferentes unidades.

```python
# create subplots
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, sharex=True)

# plot 1
ax1.scatter(xsecs, xsecs)
ax1.yaxis.set_units(secs)

# plot 2
ax2.scatter(xsecs, xsecs, yunits=hertz)

# plot 3
ax3.scatter(xsecs, xsecs, yunits=minutes)

# set labels
ax1.set_ylabel('Segundos')
ax2.set_ylabel('Hertz')
ax3.set_ylabel('Minutos')
ax3.set_xlabel('Tiempo')
```
