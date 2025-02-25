# Générez l'objet Path et en faites un patch

Ensuite, nous allons générer un objet Path et en faire un patch. Nous utiliserons l'objet Path pour tracer notre histogramme à l'aide de rectangles. Ajoutez le code suivant :

```python
XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T
barpath = path.Path.make_compound_path_from_polys(XY)
patch = patches.PathPatch(barpath)
patch.sticky_edges.y[:] = [0]
axs[0].add_patch(patch)
axs[0].autoscale_view()
```
