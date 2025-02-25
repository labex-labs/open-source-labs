# Cambiar la orientación de la gráfica

En este paso, cambiaremos la orientación de la gráfica utilizando el parámetro `orientation`. Estableceremos la orientación en `'x'` para que los tallos se proyecten a lo largo de la dirección x y la línea base se encuentre en el plano yz.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(x, y, z, bottom=-1, orientation='x')
ax.set(xlabel='x', ylabel='y', zlabel='z')

plt.show()
```
