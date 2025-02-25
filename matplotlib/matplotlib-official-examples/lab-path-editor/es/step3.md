# Crear la clase PathInteractor

En este paso, creamos la clase PathInteractor, que maneja las devoluciones de llamada de eventos para el objeto de trayectoria. Esta clase nos permite editar interactivamente la trayectoria arrastrando marcadores en el gráfico.

```python
class PathInteractor:
    """
    Un editor de trayectorias.

    Presiona 't' para alternar los marcadores de vértices encendidos y apagados. Cuando los marcadores de vértices están encendidos,
    se pueden arrastrar con el mouse.
    """

    showverts = True
    epsilon = 5  # distancia máxima en píxeles para considerarse un golpe en un vértice

    def __init__(self, pathpatch):

        self.ax = pathpatch.axes
        canvas = self.ax.figure.canvas
        self.pathpatch = pathpatch
        self.pathpatch.set_animated(True)

        x, y = zip(*self.pathpatch.get_path().vertices)

        self.line, = ax.plot(
            x, y, marker='o', markerfacecolor='r', animated=True)

        self._ind = None  # el vértice activo

        canvas.mpl_connect('draw_event', self.on_draw)
        canvas.mpl_connect('button_press_event', self.on_button_press)
        canvas.mpl_connect('key_press_event', self.on_key_press)
        canvas.mpl_connect('button_release_event', self.on_button_release)
        canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        self.canvas = canvas

    def get_ind_under_point(self, event):
        """
        Devuelve el índice del punto más cercano a la posición del evento o *None*
        si ningún punto está a una distancia de ``self.epsilon`` de la posición del evento.
        """
        xy = self.pathpatch.get_path().vertices
        xyt = self.pathpatch.get_transform().transform(xy)  # a coordenadas de visualización
        xt, yt = xyt[:, 0], xyt[:, 1]
        d = np.sqrt((xt - event.x)**2 + (yt - event.y)**2)
        ind = d.argmin()
        return ind if d[ind] < self.epsilon else None

    def on_draw(self, event):
        """Devolución de llamada para dibujos."""
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        self.ax.draw_artist(self.pathpatch)
        self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)

    def on_button_press(self, event):
        """Devolución de llamada para pulsaciones del botón del mouse."""
        if (event.inaxes is None
                or event.button!= MouseButton.LEFT
                or not self.showverts):
            return
        self._ind = self.get_ind_under_point(event)

    def on_button_release(self, event):
        """Devolución de llamada para liberaciones del botón del mouse."""
        if (event.button!= MouseButton.LEFT
                or not self.showverts):
            return
        self._ind = None

    def on_key_press(self, event):
        """Devolución de llamada para pulsaciones de teclas."""
        if not event.inaxes:
            return
        if event.key == 't':
            self.showverts = not self.showverts
            self.line.set_visible(self.showverts)
            if not self.showverts:
                self._ind = None
        self.canvas.draw()

    def on_mouse_move(self, event):
        """Devolución de llamada para movimientos del mouse."""
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
