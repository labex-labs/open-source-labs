# Definir la clase Selector

En este paso, definiremos una clase que nos permitirá seleccionar puntos del diagrama de dispersión utilizando la herramienta Selector de polígonos. Esta clase guardará los índices de los puntos seleccionados en una matriz.

```python
class SelectFromCollection:
    """
    Selecciona índices de una colección de matplotlib usando `PolygonSelector`.

    Los índices seleccionados se guardan en el atributo `ind`. Esta herramienta desvanece los
    puntos que no forman parte de la selección (es decir, reduce sus valores de alfa).
    Si su colección tiene un alfa < 1, esta herramienta cambiará permanentemente
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

        # Asegurarse de que tenemos colores separados para cada objeto
        self.fc = collection.get_facecolors()
        if len(self.fc) == 0:
            raise ValueError('La colección debe tener un color de cara')
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
