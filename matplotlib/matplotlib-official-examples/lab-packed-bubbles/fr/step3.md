# Définir la classe BubbleChart

La classe `BubbleChart` est utilisée pour créer le graphique à bulles empaquetées. La classe prend en entrée un tableau des aires des bulles et une valeur d'espacement entre les bulles. La méthode `__init__` configure les positions initiales des bulles et calcule la distance maximale de déplacement, qui est la distance que chaque bulle peut parcourir en une seule itération.

```python
class BubbleChart:
    def __init__(self, area, bubble_spacing=0):
        """
        Configuration pour l'effondrement des bulles.

        Paramètres
        ----------
        area : array-like
            Aire des bulles.
        bubble_spacing : float, valeur par défaut : 0
            Espacement minimal entre les bulles après effondrement.

        Notes
        -----
        Si "area" est trié, les résultats peuvent sembler étranges.
        """
        area = np.asarray(area)
        r = np.sqrt(area / np.pi)

        self.bubble_spacing = bubble_spacing
        self.bulles = np.ones((len(area), 4))
        self.bulles[:, 2] = r
        self.bulles[:, 3] = area
        self.maxstep = 2 * self.bulles[:, 2].max() + self.bubble_spacing
        self.step_dist = self.maxstep / 2

        # calculer la disposition initiale en grille pour les bulles
        length = np.ceil(np.sqrt(len(self.bulles)))
        grille = np.arange(length) * self.maxstep
        gx, gy = np.meshgrid(grille, grille)
        self.bulles[:, 0] = gx.flatten()[:len(self.bulles)]
        self.bulles[:, 1] = gy.flatten()[:len(self.bulles)]

        self.com = self.center_of_mass()
```
