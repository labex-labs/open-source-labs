# Crear una colección de elipses

Creamos una `EllipseCollection` con los datos anteriores y especificamos que las unidades son 'x' y los desplazamientos son `XY`.

```python
fig, ax = plt.subplots()

ec = EllipseCollection(ww, hh, aa, units='x', offsets=XY,
                       offset_transform=ax.transData)
```
