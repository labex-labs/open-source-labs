# Establecer las etiquetas de marcas predeterminadas del eje y en el lado derecho

Podemos establecer las etiquetas de marcas predeterminadas del eje y en el lado derecho de la gráfica utilizando el siguiente código:

```python
plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
plt.rcParams['ytick.left'] = plt.rcParams['ytick.labelleft'] = False
```
