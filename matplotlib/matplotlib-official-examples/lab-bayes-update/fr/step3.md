# Définir la classe UpdateDist

Ensuite, nous définissons une classe appelée `UpdateDist` qui sera utilisée pour mettre à jour la distribution bêta à mesure que de nouvelles données sont observées. La classe `UpdateDist` prend deux arguments : l'objet axe Matplotlib et la probabilité initiale de succès.

```python
class UpdateDist:
    def __init__(self, ax, prob=0.5):
        self.success = 0
        self.prob = prob
        self.line, = ax.plot([], [], 'k-')
        self.x = np.linspace(0, 1, 200)
        self.ax = ax

        # Configure les paramètres du tracé
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 10)
        self.ax.grid(True)

        # Cette ligne verticale représente la valeur théorique vers laquelle
        # la distribution tracée devrait converger.
        self.ax.axvline(prob, linestyle='--', color='black')
```

La méthode `__init__` initialise l'instance de la classe en définissant le nombre initial de succès à zéro (`self.success = 0`) et la probabilité initiale de succès à la valeur passée en argument (`self.prob = prob`). Nous créons également un objet de ligne pour représenter la distribution bêta et configurons les paramètres du tracé.

La méthode `__call__` est appelée chaque fois que l'animation est mise à jour. Elle simule une expérience de lancer de pièce et met à jour la distribution bêta en conséquence.

```python
def __call__(self, i):
        # De cette manière, le tracé peut continuer à s'exécuter et nous
        # continuons simplement à observer de nouvelles réalités du processus
        if i == 0:
            self.success = 0
            self.line.set_data([], [])
            return self.line,

        # Choisissez le succès en fonction de la dépassement d'un seuil avec un tirage uniforme
        if np.random.rand() < self.prob:
            self.success += 1
        y = beta_pdf(self.x, self.success + 1, (i - self.success) + 1)
        self.line.set_data(self.x, y)
        return self.line,
```

Si ceci est la première trame de l'animation (`if i == 0`), nous réinitialisons le nombre de succès à zéro et effaçons l'objet de ligne. Sinon, nous simulons une expérience de lancer de pièce en générant un nombre aléatoire entre 0 et 1 (`np.random.rand()`) et en le comparant à la probabilité de succès (`self.prob`). Si le nombre aléatoire est inférieur à la probabilité de succès, nous le comptons comme un succès et mettons à jour la distribution bêta en utilisant la fonction `beta_pdf`. Enfin, nous mettons à jour l'objet de ligne avec les nouvelles données et le retournons.
