# Zeichnen des Histogramms mit einem PathCollection

Anstatt viele Rectangle-Instanzen zu verwenden, können wir eine schnellere Methode verwenden, um unser Histogramm mit einem PathCollection zu zeichnen. Wir werden direkt einen zusammengesetzten Pfad mit Hilfe von Eckpunkten und Codes erstellen. Fügen Sie den folgenden Code hinzu:

```python
nrects = len(left)
nverts = nrects*(1+3+1)
verts = np.zeros((nverts, 2))
codes = np.ones(nverts, int) * path.Path.LINETO
codes[0::5] = path.Path.MOVETO
codes[4::5] = path.Path.CLOSEPOLY
verts[0::5, 0] = left
verts[0::5, 1] = bottom
verts[1::5, 0] = left
verts[1::5, 1] = top
verts[2::5, 0] = right
verts[2::5, 1] = top
verts[3::5, 0] = right
verts[3::5, 1] = bottom

barpath = path.Path(verts, codes)
patch = patches.PathPatch(barpath)
patch.sticky_edges.y[:] = [0]
axs[1].add_patch(patch)
axs[1].autoscale_view()
```
