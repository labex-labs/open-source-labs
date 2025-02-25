# Création de la classe PathInteractor

Dans cette étape, nous créons la classe PathInteractor, qui gère les rappels d'événements pour l'objet de tracé. Cette classe nous permet d'éditer le tracé de manière interactive en traînant des marqueurs sur le graphique.

```python
class PathInteractor:
    """
    Un éditeur de tracé.

    Appuyez sur 't' pour basculer les marqueurs de sommets sur et off. Lorsque les marqueurs de sommets sont activés,
    ils peuvent être traînés avec la souris.
    """

    showverts = True
    epsilon = 5  # distance maximale en pixels pour considérer qu'un sommet est touché

    def __init__(self, pathpatch):

        self.ax = pathpatch.axes
        canvas = self.ax.figure.canvas
        self.pathpatch = pathpatch
        self.pathpatch.set_animated(True)

        x, y = zip(*self.pathpatch.get_path().vertices)

        self.line, = ax.plot(
            x, y, marker='o', markerfacecolor='r', animated=True)

        self._ind = None  # le sommet actif

        canvas.mpl_connect('draw_event', self.on_draw)
        canvas.mpl_connect('button_press_event', self.on_button_press)
        canvas.mpl_connect('key_press_event', self.on_key_press)
        canvas.mpl_connect('button_release_event', self.on_button_release)
        canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        self.canvas = canvas

    def get_ind_under_point(self, event):
        """
        Retourne l'index du point le plus proche de la position de l'événement ou *None*
        si aucun point n'est à moins de ``self.epsilon`` de la position de l'événement.
        """
        xy = self.pathpatch.get_path().vertices
        xyt = self.pathpatch.get_transform().transform(xy)  # en coordonnées d'affichage
        xt, yt = xyt[:, 0], xyt[:, 1]
        d = np.sqrt((xt - event.x)**2 + (yt - event.y)**2)
        ind = d.argmin()
        return ind if d[ind] < self.epsilon else None

    def on_draw(self, event):
        """Rappel pour les dessins."""
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        self.ax.draw_artist(self.pathpatch)
        self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)

    def on_button_press(self, event):
        """Rappel pour les pressions de bouton de souris."""
        if (event.inaxes is None
                or event.button!= MouseButton.LEFT
                or not self.showverts):
            return
        self._ind = self.get_ind_under_point(event)

    def on_button_release(self, event):
        """Rappel pour les relâches de bouton de souris."""
        if (event.button!= MouseButton.LEFT
                or not self.showverts):
            return
        self._ind = None

    def on_key_press(self, event):
        """Rappel pour les pressions de touches."""
        if not event.inaxes:
            return
        if event.key == 't':
            self.showverts = not self.showverts
            self.line.set_visible(self.showverts)
            if not self.showverts:
                self._ind = None
        self.canvas.draw()

    def on_mouse_move(self, event):
        """Rappel pour les déplacements de souris."""
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
