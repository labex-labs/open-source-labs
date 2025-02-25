# Zoom

Dans cette étape, nous allons agrandir le graphique. Nous utiliserons la fonction `ginput` pour sélectionner deux coins de la zone de zoom et la fonction `waitforbuttonpress` pour terminer le zoom.

```python
tellme('Maintenant effectuez un zoom imbriqué, cliquez pour commencer')
plt.waitforbuttonpress()

while True:
    tellme('Sélectionnez deux coins du zoom, appuyez sur le bouton central de la souris pour terminer')
    pts = plt.ginput(2, timeout=-1)
    if len(pts) < 2:
        break
    (x0, y0), (x1, y1) = pts
    xmin, xmax = sorted([x0, x1])
    ymin, ymax = sorted([y0, y1])
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

tellme('Tout est fait!')
plt.show()
```
