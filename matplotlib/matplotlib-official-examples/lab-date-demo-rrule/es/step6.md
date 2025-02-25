# Graficar los datos y establecer las marcas del eje x

Finalmente, puedes graficar los datos utilizando la función `plot`, y establecer las marcas del eje x utilizando las funciones de localizador y formateador de marcas que se establecieron anteriormente.

```python
fig, ax = plt.subplots()
plt.plot(dates, s, 'o')
ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30, labelsize=10)
plt.show()
```
