# Normales Diagramm neben einem Bild

Wenn man ein Bilddiagramm mit einem festen Daten-Seitenverhältnis und der Standard-Einstellung `adjustable="box"` neben einem normalen Diagramm erstellt, sind die Achsenhöhen ungleich. `set_box_aspect()` bietet eine einfache Lösung dafür, indem es ermöglicht, dass die Achsen des normalen Diagramms die Abmessungen des Bildes als Seitenverhältnis verwenden. Dieses Beispiel zeigt auch, dass das _constrained layout_ gut mit einem festen Seitenverhältnis zusammenarbeitet.

```python
fig4, (ax, ax2) = plt.subplots(ncols=2, layout="constrained")

np.random.seed(19680801)  # Fixing random state for reproducibility
im = np.random.rand(16, 27)
ax.imshow(im)

ax2.plot([23, 45])
ax2.set_box_aspect(im.shape[0]/im.shape[1])

plt.show()
```
