# Personalizar la gráfica

En este paso, personalizaremos el diagrama de tallos tridimensional cambiando la línea base utilizando el parámetro `bottom` y cambiando el formato utilizando los parámetros `linefmt`, `markerfmt` y `basefmt`.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(
    x, y, z, linefmt='grey', markerfmt='D', bottom=np.pi)
markerline.set_markerfacecolor('none')

plt.show()
```
