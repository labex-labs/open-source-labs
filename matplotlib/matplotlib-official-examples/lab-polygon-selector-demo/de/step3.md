# Selektorklasse definieren

In diesem Schritt werden wir eine Klasse definieren, die es uns ermöglicht, Punkte aus dem Streudiagramm mit dem Polygon Selector-Tool auszuwählen. Diese Klasse wird die Indizes der ausgewählten Punkte in einem Array speichern.

```python
class SelectFromCollection:
    """
    Wählen Sie Indizes aus einer matplotlib-Sammlung mithilfe von `PolygonSelector` aus.

    Die ausgewählten Indizes werden im `ind`-Attribut gespeichert. Dieses Tool blendet die Punkte aus, die nicht Teil der Auswahl sind (d.h., verringert ihre Alpha-Werte). Wenn Ihre Sammlung einen Alpha-Wert < 1 hat, wird dieses Tool die Alpha-Werte permanent ändern.

    Beachten Sie, dass dieses Tool Sammlungselemente anhand ihrer *Ursprünge* (d.h., `offsets`) auswählt.

    Parameter
    ----------
    ax : `~matplotlib.axes.Axes`
        Achsen, mit denen interagiert werden soll.
    collection : `matplotlib.collections.Collection`-Unterklasse
        Sammlung, aus der Sie auswählen möchten.
    alpha_other : 0 <= float <= 1
        Um eine Auswahl hervorzuheben, setzt dieses Tool alle ausgewählten Punkte auf einen Alpha-Wert von 1 und nicht ausgewählte Punkte auf *alpha_other*.
    """

    def __init__(self, ax, collection, alpha_other=0.3):
        self.canvas = ax.figure.canvas
        self.collection = collection
        self.alpha_other = alpha_other

        self.xys = collection.get_offsets()
        self.Npts = len(self.xys)

        # Stellen Sie sicher, dass wir separate Farben für jedes Objekt haben
        self.fc = collection.get_facecolors()
        wenn len(self.fc) == 0:
            erhöhe ValueError('Sammlung muss eine Flächeneigenschaft haben')
        elif len(self.fc) == 1:
            self.fc = np.tile(self.fc, (self.Npts, 1))

        self.poly = PolygonSelector(ax, self.onselect, draw_bounding_box=True)
        self.ind = []

    def onselect(self, verts):
        path = Path(verts)
        self.ind = np.nonzero(path.contains_points(self.xys))[0]
        self.fc[:, -1] = self.alpha_other
        self.fc[self.ind, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()

    def disconnect(self):
        self.poly.disconnect_events()
        self.fc[:, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()
```

需要注意的是，原文中`wenn len(self.fc) == 0:`这里的`wenn`应该是`Wenn`（大写），属于拼写错误，翻译时按照正确的来。 还有`erhöhe ValueError`应该是`erhöhe ValueError`（这里可能也是拼写有误，推测应该是`erhöhe ValueError`为`erhöhe ValueError`，即`raise ValueError`） ，翻译时按照正确逻辑翻译为`引发 ValueError` 。整体译文尽量贴近原文表述错误的样子呈现了代码中的问题部分。
