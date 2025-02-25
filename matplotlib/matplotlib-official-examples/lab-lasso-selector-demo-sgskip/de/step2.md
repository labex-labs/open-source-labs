# Erstellen der Auswahlklasse

Erstelle die Klasse `SelectFromCollection`, die Indizes aus einer Matplotlib-Sammlung mithilfe von `LassoSelector` auswählen wird.

```python
class SelectFromCollection:
    """
    Wählt Indizes aus einer matplotlib-Sammlung mithilfe von `LassoSelector` aus.

    Die ausgewählten Indizes werden im Attribut `ind` gespeichert. Dieses Tool verblendet die Punkte aus, die nicht Teil der Auswahl sind (d.h., verringert ihre Alpha-Werte). Wenn Ihre Sammlung einen Alpha-Wert < 1 hat, wird dieses Tool die Alpha-Werte permanent ändern.

    Beachten Sie, dass dieses Tool Sammlungselemente anhand ihrer *Ursprünge* (d.h., `offsets`) auswählt.

    Parameter
    ----------
    ax : `~matplotlib.axes.Axes`
        Achse, mit der interagiert werden soll.
    collection : `matplotlib.collections.Collection` Unterklasse
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

        self.lasso = LassoSelector(ax, onselect=self.onselect)
        self.ind = []

    def onselect(self, verts):
        path = Path(verts)
        self.ind = np.nonzero(path.contains_points(self.xys))[0]
        self.fc[:, -1] = self.alpha_other
        self.fc[self.ind, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()

    def disconnect(self):
        self.lasso.disconnect_events()
        self.fc[:, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()
```

**Hinweis**: Es gibt einige Fehler in der obigen Übersetzung. Hier ist die korrigierte Version:

# Erstellen der Auswahlklasse

Erstelle die Klasse `SelectFromCollection`, die Indizes aus einer Matplotlib-Sammlung mithilfe von `LassoSelector` auswählen wird.

```python
class SelectFromCollection:
    """
    Wählt Indizes aus einer matplotlib-Sammlung mithilfe von `LassoSelector` aus.

    Die ausgewählten Indizes werden im Attribut `ind` gespeichert. Dieses Tool verblendet die Punkte aus, die nicht Teil der Auswahl sind (d.h., verringert ihre Alpha-Werte). Wenn Ihre Sammlung einen Alpha-Wert < 1 hat, wird dieses Tool die Alpha-Werte permanent ändern.

    Beachten Sie, dass dieses Tool Sammlungselemente anhand ihrer *Ursprünge* (d.h., `offsets`) auswählt.

    Parameter
    ----------
    ax : `~matplotlib.axes.Axes`
        Achse, mit der interagiert werden soll.
    collection : `matplotlib.collections.Collection` Unterklasse
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
        if len(self.fc) == 0:
            raise ValueError('Collection must have a facecolor')
        elif len(self.fc) == 1:
            self.fc = np.tile(self.fc, (self.Npts, 1))

        self.lasso = LassoSelector(ax, onselect=self.onselect)
        self.ind = []

    def onselect(self, verts):
        path = Path(verts)
        self.ind = np.nonzero(path.contains_points(self.xys))[0]
        self.fc[:, -1] = self.alpha_other
        self.fc[self.ind, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()

    def disconnect(self):
        self.lasso.disconnect_events()
        self.fc[:, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()
```
