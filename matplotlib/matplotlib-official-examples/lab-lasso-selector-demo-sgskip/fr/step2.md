# Créer la classe Sélecteur

Créez la classe `SelectFromCollection` qui sélectionnera des indices à partir d'une collection Matplotlib en utilisant `LassoSelector`.

```python
class SelectFromCollection:
    """
    Sélectionnez des indices à partir d'une collection matplotlib en utilisant `LassoSelector`.

    Les indices sélectionnés sont enregistrés dans l'attribut `ind`. Cet outil assombrit les
    points qui ne font pas partie de la sélection (c'est-à-dire réduit leurs valeurs d'alpha).
    Si votre collection a un alpha < 1, cet outil modifiera définitivement les valeurs d'alpha.

    Notez que cet outil sélectionne les objets de collection en fonction de leurs *origine*
    (c'est-à-dire `offsets`).

    Paramètres
    ----------
    ax : `~matplotlib.axes.Axes`
        Axes avec lequel interagir.
    collection : `matplotlib.collections.Collection` sous-classe
        Collection à partir de laquelle vous voulez sélectionner.
    alpha_other : 0 <= float <= 1
        Pour mettre en évidence une sélection, cet outil définit tous les points sélectionnés
        à une valeur d'alpha de 1 et les points non sélectionnés à *alpha_other*.
    """

    def __init__(self, ax, collection, alpha_other=0.3):
        self.canvas = ax.figure.canvas
        self.collection = collection
        self.alpha_other = alpha_other

        self.xys = collection.get_offsets()
        self.Npts = len(self.xys)

        # Assurez-vous d'avoir des couleurs distinctes pour chaque objet
        self.fc = collection.get_facecolors()
        if len(self.fc) == 0:
            raise ValueError('La collection doit avoir une couleur de face')
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
