# Generieren des Path-Objekts und Erstellen eines Patches daraus

Als nächstes werden wir ein Path-Objekt generieren und daraus einen Patch erstellen. Wir werden das Path-Objekt verwenden, um unser Histogramm mit Rechtecken zu zeichnen. Fügen Sie den folgenden Code hinzu:

```python
XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T
barpath = path.Path.make_compound_path_from_polys(XY)
patch = patches.PathPatch(barpath)
patch.sticky_edges.y[:] = [0]
axs[0].add_patch(patch)
axs[0].autoscale_view()
```
