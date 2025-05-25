# Definir Classe Seletora

Nesta etapa, definiremos uma classe que nos permitirá selecionar pontos do gráfico de dispersão usando a ferramenta Polygon Selector. Esta classe salvará os índices dos pontos selecionados em um array.

```python
class SelectFromCollection:
    """
    Seleciona índices de uma coleção matplotlib usando `PolygonSelector`.

    Os índices selecionados são salvos no atributo `ind`. Esta ferramenta atenua os
    pontos que não fazem parte da seleção (ou seja, reduz seus valores alfa). Se sua
    coleção tiver alfa < 1, esta ferramenta alterará permanentemente os valores alfa.

    Observe que esta ferramenta seleciona objetos de coleção com base em suas *origens*
    (ou seja, `offsets`).

    Parâmetros
    ----------
    ax : `~matplotlib.axes.Axes`
        Eixos para interagir.
    collection : subclasse `matplotlib.collections.Collection`
        Coleção da qual você deseja selecionar.
    alpha_other : 0 <= float <= 1
        Para destacar uma seleção, esta ferramenta define todos os pontos selecionados para um
        valor alfa de 1 e pontos não selecionados para *alpha_other*.
    """

    def __init__(self, ax, collection, alpha_other=0.3):
        self.canvas = ax.figure.canvas
        self.collection = collection
        self.alpha_other = alpha_other

        self.xys = collection.get_offsets()
        self.Npts = len(self.xys)

        # Ensure that we have separate colors for each object
        self.fc = collection.get_facecolors()
        if len(self.fc) == 0:
            raise ValueError('Collection must have a facecolor')
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
