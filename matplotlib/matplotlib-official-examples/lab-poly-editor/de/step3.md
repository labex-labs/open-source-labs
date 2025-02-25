# Erstellen der PolygonInteractor-Klasse

Wir müssen die `PolygonInteractor`-Klasse erstellen, die die Hauptklasse für den Polygon-Editor ist. Diese Klasse wird alle Interaktionen mit dem Polygon behandeln, wie das Verschieben, Löschen und Einfügen von Eckpunkten.

```python
class PolygonInteractor:
    """
    Ein Polygon-Editor.

    Tastatureingaben

      't' um die Anzeige von Eckpunkten an- und auszuschalten. Wenn die Eckpunkte angezeigt werden,
          können Sie sie verschieben und löschen

      'd' um den Eckpunkt unterhalb des Mauszeigers zu löschen

      'i' um einen Eckpunkt an der aktuellen Position einzufügen. Sie müssen sich innerhalb von
          einem bestimmten Abstand (epsilon) von der Linie zwischen zwei vorhandenen Eckpunkten befinden

    """

    showverts = True
    epsilon = 5  # maximale Pixelabstand, um als Treffer eines Eckpunkts zu gelten

    def __init__(self, ax, poly):
        if poly.figure is None:
            raise RuntimeError('Sie müssen das Polygon zuerst einer Figur '
                               'oder einem Canvas hinzufügen, bevor Sie den Interaktor definieren')
        self.ax = ax
        canvas = poly.figure.canvas
        self.poly = poly

        x, y = zip(*self.poly.xy)
        self.line = Line2D(x, y,
                           marker='o', markerfacecolor='r',
                           animated=True)
        self.ax.add_line(self.line)

        self.cid = self.poly.add_callback(self.poly_changed)
        self._ind = None  # der aktive Eckpunkt

        canvas.mpl_connect('draw_event', self.on_draw)
        canvas.mpl_connect('button_press_event', self.on_button_press)
        canvas.mpl_connect('key_press_event', self.on_key_press)
        canvas.mpl_connect('button_release_event', self.on_button_release)
        canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        self.canvas = canvas

    def on_draw(self, event):
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        self.ax.draw_artist(self.poly)
        self.ax.draw_artist(self.line)
        # Hier ist kein Blit erforderlich, da dies vor dem Aktualisieren des Bildschirms erfolgt

    def poly_changed(self, poly):
        """Diese Methode wird aufgerufen, wenn das Pathpatch-Objekt geändert wird."""
        # Kopieren Sie nur die Künstler-Eigenschaften auf die Linie (außer Sichtbarkeit)
        vis = self.line.get_visible()
        Artist.update_from(self.line, poly)
        self.line.set_visible(vis)  # Verwenden Sie den Sichtbarkeitsstatus des Polygons nicht

    def get_ind_under_point(self, event):
        """
        Gibt den Index des Punkts zurück, der am nächsten an der Ereignisposition liegt, oder *None*,
        wenn kein Punkt innerhalb von ``self.epsilon`` von der Ereignisposition entfernt ist.
        """
        # Anzeige-Koordinaten
        xy = np.asarray(self.poly.xy)
        xyt = self.poly.get_transform().transform(xy)
        xt, yt = xyt[:, 0], xyt[:, 1]
        d = np.hypot(xt - event.x, yt - event.y)
        indseq, = np.nonzero(d == d.min())
        ind = indseq[0]

        if d[ind] >= self.epsilon:
            ind = None

        return ind

    def on_button_press(self, event):
        """Callback für Mausklick-Ereignisse."""
        if not self.showverts:
            return
        if event.inaxes is None:
            return
        if event.button!= 1:
            return
        self._ind = self.get_ind_under_point(event)

    def on_button_release(self, event):
        """Callback für Maus loslassen-Ereignisse."""
        if not self.showverts:
            return
        if event.button!= 1:
            return
        self._ind = None

    def on_key_press(self, event):
        """Callback für Tastatureingaben."""
        if not event.inaxes:
            return
        if event.key == 't':
            self.showverts = not self.showverts
            self.line.set_visible(self.showverts)
            if not self.showverts:
                self._ind = None
        elif event.key == 'd':
            ind = self.get_ind_under_point(event)
            if ind is not None:
                self.poly.xy = np.delete(self.poly.xy,
                                         ind, axis=0)
                self.line.set_data(zip(*self.poly.xy))
        elif event.key == 'i':
            xys = self.poly.get_transform().transform(self.poly.xy)
            p = event.x, event.y  # Anzeige-Koordinaten
            for i in range(len(xys) - 1):
                s0 = xys[i]
                s1 = xys[i + 1]
                d = dist_point_to_segment(p, s0, s1)
                if d <= self.epsilon:
                    self.poly.xy = np.insert(
                        self.poly.xy, i+1,
                        [event.xdata, event.ydata],
                        axis=0)
                    self.line.set_data(zip(*self.poly.xy))
                    break
        if self.line.stale:
            self.canvas.draw_idle()

    def on_mouse_move(self, event):
        """Callback für Mausbewegungen."""
        if not self.showverts:
            return
        if self._ind is None:
            return
        if event.inaxes is None:
            return
        if event.button!= 1:
            return
        x, y = event.xdata, event.ydata

        self.poly.xy[self._ind] = x, y
        if self._ind == 0:
            self.poly.xy[-1] = x, y
        elif self._ind == len(self.poly.xy) - 1:
            self.poly.xy[0] = x, y
        self.line.set_data(zip(*self.poly.xy))

        self.canvas.restore_region(self.background)
        self.ax.draw_artist(self.poly)
        self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)
```
