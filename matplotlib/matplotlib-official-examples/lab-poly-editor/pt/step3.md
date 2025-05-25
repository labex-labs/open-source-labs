# Criar a Classe PolygonInteractor

Precisamos criar a classe `PolygonInteractor`, que é a classe principal para o editor de polígonos. Esta classe irá lidar com todas as interações com o polígono, como mover, deletar e inserir vértices.

```python
class PolygonInteractor:
    """
    Um editor de polígonos.

    Atalhos de teclado

      't' alterna os marcadores de vértice ligados e desligados. Quando os marcadores de vértice estão ligados,
          você pode movê-los, excluí-los

      'd' exclui o vértice sob o ponto

      'i' insere um vértice no ponto. Você deve estar dentro de epsilon da
          linha que conecta dois vértices existentes

    """

    showverts = True
    epsilon = 5  # distância máxima em pixels para contar como um acerto de vértice

    def __init__(self, ax, poly):
        if poly.figure is None:
            raise RuntimeError('Você deve primeiro adicionar o polígono a uma figura '
                               'ou tela antes de definir o interator')
        self.ax = ax
        canvas = poly.figure.canvas
        self.poly = poly

        x, y = zip(*self.poly.xy)
        self.line = Line2D(x, y,
                           marker='o', markerfacecolor='r',
                           animated=True)
        self.ax.add_line(self.line)

        self.cid = self.poly.add_callback(self.poly_changed)
        self._ind = None  # o vértice ativo

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
        # não precisa de blit aqui, isso será acionado antes que a tela seja
        # atualizada

    def poly_changed(self, poly):
        """Este método é chamado sempre que o objeto pathpatch é chamado."""
        # apenas copie as propriedades do artista para a linha (exceto visibilidade)
        vis = self.line.get_visible()
        Artist.update_from(self.line, poly)
        self.line.set_visible(vis)  # não use o estado de visibilidade do polígono

    def get_ind_under_point(self, event):
        """
        Retorna o índice do ponto mais próximo da posição do evento ou *None*
        se nenhum ponto estiver dentro de ``self.epsilon`` da posição do evento.
        """
        # coordenadas de exibição
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
        """Callback para pressionamentos de botão do mouse."""
        if not self.showverts:
            return
        if event.inaxes is None:
            return
        if event.button != 1:
            return
        self._ind = self.get_ind_under_point(event)

    def on_button_release(self, event):
        """Callback para liberações de botão do mouse."""
        if not self.showverts:
            return
        if event.button != 1:
            return
        self._ind = None

    def on_key_press(self, event):
        """Callback para pressionamentos de tecla."""
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
            p = event.x, event.y  # display coords
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
        """Callback para movimentos do mouse."""
        if not self.showverts:
            return
        if self._ind is None:
            return
        if event.inaxes is None:
            return
        if event.button != 1:
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
