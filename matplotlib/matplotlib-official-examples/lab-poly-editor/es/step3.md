# Crear la clase PolygonInteractor

Necesitamos crear la clase `PolygonInteractor`, que es la clase principal para el editor de polígonos. Esta clase manejará todas las interacciones con el polígono, como mover, eliminar e insertar vértices.

```python
class PolygonInteractor:
    """
    Un editor de polígonos.

    Comandos de teclado

      't' alternar la visualización de los marcadores de vértices. Cuando los
          marcadores de vértices están activos, se pueden mover y eliminar

      'd' eliminar el vértice debajo del punto

      'i' insertar un vértice en el punto. Debes estar dentro de una distancia
          epsilon de la línea que conecta dos vértices existentes

    """

    showverts = True
    epsilon = 5  # distancia máxima en píxeles para considerar que se ha golpeado un vértice

    def __init__(self, ax, poly):
        if poly.figure is None:
            raise RuntimeError('Debes agregar primero el polígono a una figura '
                               'o lienzo antes de definir el interactuador')
        self.ax = ax
        canvas = poly.figure.canvas
        self.poly = poly

        x, y = zip(*self.poly.xy)
        self.line = Line2D(x, y,
                           marker='o', markerfacecolor='r',
                           animated=True)
        self.ax.add_line(self.line)

        self.cid = self.poly.add_callback(self.poly_changed)
        self._ind = None  # el vértice activo

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
        # no es necesario hacer un blit aquí, esto se ejecutará antes de que se actualice la pantalla

    def poly_changed(self, poly):
        """Este método se llama cada vez que se llama al objeto pathpatch."""
        # solo copiar las propiedades del artista a la línea (excepto la visibilidad)
        vis = self.line.get_visible()
        Artist.update_from(self.line, poly)
        self.line.set_visible(vis)  # no usar el estado de visibilidad del polígono

    def get_ind_under_point(self, event):
        """
        Devuelve el índice del punto más cercano a la posición del evento o *None*
        si ningún punto está a una distancia menor o igual a ``self.epsilon`` de la
        posición del evento.
        """
        # coordenadas de visualización
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
        """Callback para pulsaciones de botón del ratón."""
        if not self.showverts:
            return
        if event.inaxes is None:
            return
        if event.button!= 1:
            return
        self._ind = self.get_ind_under_point(event)

    def on_button_release(self, event):
        """Callback para liberaciones de botón del ratón."""
        if not self.showverts:
            return
        if event.button!= 1:
            return
        self._ind = None

    def on_key_press(self, event):
        """Callback para pulsaciones de teclas."""
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
            p = event.x, event.y  # coordenadas de visualización
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
        """Callback para movimientos del ratón."""
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
