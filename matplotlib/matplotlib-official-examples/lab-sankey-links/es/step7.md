# Agregar el primer diagrama

Agregamos el primer diagrama usando `sankey.add()` con `flows=[1, -1]` y `orientations=[0, 1]`.

```python
sankey.add(flows=[1, -1], orientations=[0, 1],
           patchlabel="0", facecolor='k',
           rotation=45)
```
