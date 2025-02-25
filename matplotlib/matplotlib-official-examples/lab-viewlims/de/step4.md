# Erstellen des Diagramms

Wir werden das Diagramm erstellen, indem wir zuerst das Bild mithilfe der MandelbrotDisplay-Klasse berechnen und dann zwei identische Panels mit Hilfe von `subplots` erstellen. Wir werden das Bild zu beiden Panels mit `imshow` hinzufügen und das UpdatingRect-Objekt zum linken Panel hinzufügen.

```python
md = MandelbrotDisplay()
Z = md.compute_image(-2., 0.5, -1.25, 1.25)

fig1, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(Z, origin='lower',
           extent=(md.x.min(), md.x.max(), md.y.min(), md.y.max()))
ax2.imshow(Z, origin='lower',
           extent=(md.x.min(), md.x.max(), md.y.min(), md.y.max()))

rect = UpdatingRect(
    [0, 0], 0, 0, facecolor='none', edgecolor='black', linewidth=1.0)
rect.set_bounds(*ax2.viewLim.bounds)
ax1.add_patch(rect)
```
