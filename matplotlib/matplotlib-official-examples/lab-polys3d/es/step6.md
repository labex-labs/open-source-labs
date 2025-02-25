# Crear los polígonos y agregarlos a la trama

Creamos los polígonos utilizando la función `PolyCollection` de Matplotlib y los agregamos a la trama.

```python
poly = PolyCollection(verts, facecolors=facecolors, alpha=.7)
ax.add_collection3d(poly, zs=lambdas, zdir='y')
```
