# Generar el objeto Path y crear un recuadro a partir de él

A continuación, generaremos un objeto Path y crearemos un recuadro a partir de él. Usaremos el objeto Path para dibujar nuestro histograma usando rectángulos. Agrega el siguiente código:

```python
XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T
barpath = path.Path.make_compound_path_from_polys(XY)
patch = patches.PathPatch(barpath)
patch.sticky_edges.y[:] = [0]
axs[0].add_patch(patch)
axs[0].autoscale_view()
```
