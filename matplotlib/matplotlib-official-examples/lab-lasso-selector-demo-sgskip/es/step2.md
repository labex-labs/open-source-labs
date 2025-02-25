# Crear la clase Selector

Crea la clase `SelectFromCollection` que seleccionará índices de una colección de Matplotlib utilizando `LassoSelector`.

```python
class SelectFromCollection:
    """
    Selecciona índices de una colección de matplotlib utilizando `LassoSelector`.

    Los índices seleccionados se guardan en el atributo `ind`. Esta herramienta desvanece los
    puntos que no forman parte de la selección (es decir, reduce sus valores de alfa).
    Si su colección tiene un alfa < 1, esta herramienta modificará permanentemente
    los valores de alfa.

    Tenga en cuenta que esta herramienta selecciona objetos de colección basados en sus *orígenes*
    (es decir, `offsets`).

    Parámetros
    ----------
    ax : `~matplotlib.axes.Axes`
        Ejes con los que interactuar.
    collection : `matplotlib.collections.Collection` subclase
        Colección de la que desea seleccionar.
    alpha_other : 0 <= float <= 1
        Para resaltar una selección, esta herramienta establece todos los puntos seleccionados
        a un valor de alfa de 1 y los puntos no seleccionados a *alpha_other*.
    """

    def __init__(self, ax, collection, alpha_other=0.3):
        self.canvas = ax.figure.canvas
        self.collection = collection
        self.alpha_other = alpha_other

        self.xys = collection.get_offsets()
        self.Npts = len(self.xys)

        # Asegúrese de que tengamos colores separados para cada objeto
        self.fc = collection.get_facecolors()
        if len(self.fc) == 0:
            raise ValueError('La colección debe tener un color de cara')
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
