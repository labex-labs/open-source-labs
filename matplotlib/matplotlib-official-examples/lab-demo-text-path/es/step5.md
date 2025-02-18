# Crear una caja de desplazamiento anclada (anchored offset box)

Crea una caja de desplazamiento anclada utilizando `AnnotationBbox` para agregar la caja de desplazamiento y establecer su posición. Utiliza el siguiente código para crear la caja de desplazamiento anclada:

```python
ao = AnchoredOffsetbox(loc='upper left', child=offsetbox, frameon=True,
                           borderpad=0.2)
ax1.add_artist(ao)
```
