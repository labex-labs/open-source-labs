# Créez la classe PolygonInteractor

Nous devons créer la classe `PolygonInteractor`, qui est la classe principale pour l'éditeur de polygone. Cette classe gérera toutes les interactions avec le polygone, telles que le déplacement, la suppression et l'insertion de sommets.

```python
class PolygonInteractor:
    """
    Un éditeur de polygone.

    Liaisons de touches

      't' bascule les marqueurs de sommet sur et off. Lorsque les marqueurs de sommet sont activés,
          vous pouvez les déplacer, les supprimer

      'd' supprime le sommet sous le point

      'i' insère un sommet au point. Vous devez être à une distance epsilon de
          la ligne reliant deux sommets existants

    """

    showverts = True
    epsilon = 5  # distance maximale en pixels pour considérer qu'un sommet est touché

    def __init__(self, ax, poly):
        if poly.figure is None:
            raise RuntimeError('Vous devez d\'abord ajouter le polygone à une figure '
                               'ou un canevas avant de définir l\'interacteur')
        self.ax = ax
        canvas = poly.figure.canvas
        self.poly = poly

        x, y = zip(*self.poly.xy)
        self.line = Line2D(x, y,
                           marker='o', markerfacecolor='r',
                           animated=True)
        self.ax.add_line(self.line)

        self.cid = self.poly.add_callback(self.poly_changed)
        self._ind = None  # le sommet actif

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
        # pas besoin de blit ici, cela se produira avant que l'écran ne soit
        # mis à jour

    def poly_changed(self, poly):
        """Cette méthode est appelée chaque fois que l'objet pathpatch est appelé."""
        # seulement copiez les propriétés de l'artiste vers la ligne (sauf la visibilité)
        vis = self.line.get_visible()
        Artist.update_from(self.line, poly)
        self.line.set_visible(vis)  # n'utilisez pas l'état de visibilité du polygone

    def get_ind_under_point(self, event):
        """
        Retourne l'index du point le plus proche de la position de l'événement ou *None*
        si aucun point n'est à une distance inférieure à ``self.epsilon`` de la position de l'événement.
        """
        # coordonnées d'affichage
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
        """Callback pour les pressions de bouton de souris."""
        if not self.showverts:
            return
        if event.inaxes is None:
            return
        if event.button!= 1:
            return
        self._ind = self.get_ind_under_point(event)

    def on_button_release(self, event):
        """Callback pour les relâchements de bouton de souris."""
        if not self.showverts:
            return
        if event.button!= 1:
            return
        self._ind = None

    def on_key_press(self, event):
        """Callback pour les pressions de touches."""
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
            p = event.x, event.y  # coordonnées d'affichage
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
        """Callback pour les déplacements de souris."""
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
