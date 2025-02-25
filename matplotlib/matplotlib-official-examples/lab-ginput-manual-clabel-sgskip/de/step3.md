# Zoomen

In diesem Schritt werden wir das Diagramm vergrößern. Wir werden die `ginput`-Funktion verwenden, um zwei Ecken der Zoom-Box auszuwählen, und die `waitforbuttonpress`-Funktion, um den Zoom abzuschließen.

```python
tellme('Jetzt mache einen geschachtelten Zoom, klicke, um zu beginnen')
plt.waitforbuttonpress()

while True:
    tellme('Wähle zwei Ecken des Zooms, mittlere Maustaste, um zu beenden')
    pts = plt.ginput(2, timeout=-1)
    if len(pts) < 2:
        break
    (x0, y0), (x1, y1) = pts
    xmin, xmax = sorted([x0, x1])
    ymin, ymax = sorted([y0, y1])
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

tellme('Alles erledigt!')
plt.show()
```
