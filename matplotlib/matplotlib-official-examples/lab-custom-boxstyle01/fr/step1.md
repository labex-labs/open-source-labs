# Implémenter un style de boîte personnalisé sous forme de fonction

Les styles de boîte personnalisés peuvent être implémentés sous forme de fonctions qui prennent des arguments spécifiant à la fois une boîte rectangulaire et la quantité de "mutation", et renvoient le chemin "muté". Ici, nous allons implémenter un style de boîte personnalisé qui renvoie un nouveau chemin qui ajoute une forme "flèche" à gauche de la boîte.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import BoxStyle
from matplotlib.path import Path

def custom_box_style(x0, y0, width, height, mutation_size):
    """
    Étant donné l'emplacement et la taille de la boîte, renvoie le chemin de la boîte autour
    de celle-ci.

    La rotation est automatiquement prise en compte.

    Paramètres
    ----------
    x0, y0, width, height : float
        Emplacement et taille de la boîte.
    mutation_size : float
        Échelle de référence de mutation, généralement la taille de police du texte.
    """
    # padding
    mypad = 0.3
    pad = mutation_size * mypad
    # largeur et hauteur avec padding ajouté.
    width = width + 2 * pad
    height = height + 2 * pad
    # limite de la boîte avec padding
    x0, y0 = x0 - pad, y0 - pad
    x1, y1 = x0 + width, y0 + height
    # renvoie le nouveau chemin
    return Path([(x0, y0),
                 (x1, y0), (x1, y1), (x0, y1),
                 (x0-pad, (y0+y1)/2), (x0, y0),
                 (x0, y0)],
                closed=True)

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle=custom_box_style, alpha=0.2))
plt.show()
```
