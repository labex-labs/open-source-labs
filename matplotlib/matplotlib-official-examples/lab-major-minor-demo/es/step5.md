# Selección automática de marcas principales y secundarias

```python
# Crea datos
t = np.arange(0.0, 100.0, 0.01)
s = np.sin(2 * np.pi * t) * np.exp(-t * 0.01)

# Grafica los datos
fig, ax = plt.subplots()
ax.plot(t, s)

# Establece el localizador secundario
ax.xaxis.set_minor_locator(AutoMinorLocator())

# Establece los parámetros de las marcas
ax.tick_params(which='both', width=2)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4, color='r')

# Muestra la gráfica
plt.show()
```

En este paso, creamos nuevos datos y los graficamos. Luego establecemos el localizador secundario para seleccionar automáticamente el número de marcas secundarias. Después, establecemos los parámetros de las marcas, es decir, el ancho y la longitud de las marcas y su color, para las marcas principales y secundarias. Finalmente, mostramos la gráfica.
