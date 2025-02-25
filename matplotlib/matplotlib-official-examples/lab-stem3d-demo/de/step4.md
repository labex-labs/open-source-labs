# Anpassen des Diagramms

In diesem Schritt passen wir das 3D-Stammdiagramm an, indem wir die Grundlinie mithilfe des Parameters `bottom` ändern und das Format mithilfe der Parameter `linefmt`, `markerfmt` und `basefmt` ändern.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(
    x, y, z, linefmt='grey', markerfmt='D', bottom=np.pi)
markerline.set_markerfacecolor('none')

plt.show()
```
