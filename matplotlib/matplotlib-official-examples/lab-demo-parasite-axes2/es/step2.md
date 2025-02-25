# Crear ejes principal y parasitos

Crearemos un eje principal y dos ejes parasitos utilizando las funciones `host_subplot()` y `twinx()`. La función `host_subplot()` crea un eje principal, y la función `twinx()` crea ejes parasitos que comparten el mismo eje x con el eje principal.

```python
host = host_subplot(111, axes_class=axisartist.Axes)
plt.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()
```
