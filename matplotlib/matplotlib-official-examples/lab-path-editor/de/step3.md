# Die PathInteractor-Klasse erstellen

In diesem Schritt erstellen wir die PathInteractor-Klasse, die die Ereignisrufe für das Pfadobjekt behandelt. Diese Klasse ermöglicht es uns, den Pfad interaktiv zu bearbeiten, indem wir Marker auf dem Graphen ziehen.

```python
class PathInteractor:
    """
    Ein Pfad-Editor.

    Drücken Sie 't', um die Eckmarkierungen an- und auszuschalten. Wenn die Eckmarkierungen aktiviert sind,
    können Sie sie mit der Maus ziehen.
    """

    showverts = True
    epsilon = 5  # maximale Pixelabstand, um als Eckpunkt-Treffer zu gelten

    def __init__(self, pathpatch):

        self.ax = pathpatch.axes
        canvas = self.ax.figure.canvas
        self.pathpatch = pathpatch
        self.pathpatch.set_animated(True)

        x, y = zip(*self.pathpatch.get_path().vertices)

        self.line, = ax.plot(
            x, y, marker='o', markerfacecolor='r', animated=True)

        self._ind = None  # der aktive Eckpunkt

        canvas.mpl_connect('draw_event', self.on_draw)
        canvas.mpl_connect('button_press_event', self.on_button_press)
        canvas.mpl_connect('key_press_event', self.on_key_press)
        canvas.mpl_connect('button_release_event', self.on_button_release)
        canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        self.canvas = canvas

    def get_ind_under_point(self, event):
        """
        Gibt den Index des Punkts zurück, der am nächsten an der Ereignisposition liegt, oder *None*,
        wenn kein Punkt innerhalb von ``self.epsilon`` zur Ereignisposition liegt.
        """
        xy = self.pathpatch.get_path().vertices
        xyt = self.pathpatch.get_transform().transform(xy)  # in die Anzeige-Koordinaten
        xt, yt = xyt[:, 0], xyt[:, 1]
        d = np.sqrt((xt - event.x)**2 + (yt - event.y)**2)
        ind = d.argmin()
        return ind if d[ind] < self.epsilon else None

    def on_draw(self, event):
        """Ruf für Zeichnungen."""
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        self.ax.draw_artist(self.pathpatch)
        self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)

    def on_button_press(self, event):
        """Ruf für Mausklick-Ereignisse."""
        if (event.inaxes is None
                or event.button!= MouseButton.LEFT
                or not self.showverts):
            return
        self._ind = self.get_ind_under_point(event)

    def on_button_release(self, event):
        """Ruf für Maus loslassen-Ereignisse."""
        if (event.button!= MouseButton.LEFT
                or not self.showverts):
            return
        self._ind = None

    def on_key_press(self, event):
        """Ruf für Tastendrücke."""
        if not event.inaxes:
            return
        if event.key == 't':
            self.showverts = not self.showverts
            self.line.set_visible(self.showverts)
            if not self.showverts:
                self._ind = None
        self.canvas.draw()

    def on_mouse_move(self, event):
        """Ruf für Mausbewegungen."""
        if (self._ind is None
                or event.inaxes is None
                or event.button!= MouseButton.LEFT
                or not self.showverts):
            return

        vertices = self.pathpatch.get_path().vertices

        vertices[self._ind] = event.xdata, event.ydata
        self.line.set_data(zip(*vertices))

        self.canvas.restore_region(self.background)
        self.ax.draw_artist(self.pathpatch)
        self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)
```
