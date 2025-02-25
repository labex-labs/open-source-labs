# Rellenando los diagramas de caja con colores personalizados

A continuación, rellenaremos los diagramas de caja con colores personalizados. Crearemos una lista de colores y usaremos un bucle para rellenar cada caja con un color diferente.

```python
colors = ['pink', 'lightblue', 'lightgreen']
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
```
