# Definieren der BubbleChart-Klasse

Die `BubbleChart`-Klasse wird verwendet, um das gepackte Blasen-Diagramm zu erstellen. Die Klasse nimmt ein Array von Blasenflächen und einen Blasenabstandswert entgegen. Die `__init__`-Methode setzt die Anfangspositionen der Blasen und berechnet die maximale Schrittweite, die die Entfernung ist, die jede Blase in einer einzelnen Iteration bewegen kann.

```python
class BubbleChart:
    def __init__(self, area, bubble_spacing=0):
        """
        Setup for bubble collapse.

        Parameters
        ----------
        area : array-like
            Fläche der Blasen.
        bubble_spacing : float, Standardwert: 0
            Minimaler Abstand zwischen den Blasen nach dem Zusammenfallen.

        Notes
        -----
        Wenn "area" sortiert ist, können die Ergebnisse merkwürdig aussehen.
        """
        area = np.asarray(area)
        r = np.sqrt(area / np.pi)

        self.bubble_spacing = bubble_spacing
        self.bubbles = np.ones((len(area), 4))
        self.bubbles[:, 2] = r
        self.bubbles[:, 3] = area
        self.maxstep = 2 * self.bubbles[:, 2].max() + self.bubble_spacing
        self.step_dist = self.maxstep / 2

        # berechne die Anfangs-Gitterlayout für die Blasen
        length = np.ceil(np.sqrt(len(self.bubbles)))
        grid = np.arange(length) * self.maxstep
        gx, gy = np.meshgrid(grid, grid)
        self.bubbles[:, 0] = gx.flatten()[:len(self.bubbles)]
        self.bubbles[:, 1] = gy.flatten()[:len(self.bubbles)]

        self.com = self.center_of_mass()
```
