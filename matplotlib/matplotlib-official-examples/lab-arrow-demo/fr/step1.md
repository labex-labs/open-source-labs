# Importation des bibliothèques et définition de la fonction

La première étape consiste à importer les bibliothèques nécessaires et à définir la fonction `make_arrow_graph()`. Cette fonction prend différents paramètres tels que les axes, les données, la taille, l'affichage, la forme, la largeur maximale de flèche, l'espacement entre les flèches, l'alpha, la normalisation des données, la couleur du contour, la couleur des étiquettes et les kwargs. Elle utilise ces paramètres pour créer un graphique d'flèches.

```python
# Importation des bibliothèques
import itertools
import matplotlib.pyplot as plt
import numpy as np

# Définition de la fonction
def make_arrow_graph(ax, data, size=4, display='length', shape='right',
                     max_arrow_width=0.03, arrow_sep=0.02, alpha=0.5,
                     normalize_data=False, ec=None, labelcolor=None,
                     **kwargs):
    """
    Crée un graphique d'flèches.

    Paramètres
    ----------
    ax
        Les axes sur lesquels le graphique est tracé.
    data
        Dictionnaire avec les probabilités pour les bases et les transitions entre paires.
    size
        Taille du graphique, en pouces.
    display : {'length', 'width', 'alpha'}
        La propriété de la flèche à modifier.
    shape : {'full', 'left', 'right'}
        Pour les flèches complètes ou semi-complètes.
    max_arrow_width : float
        Largeur maximale d'une flèche, en coordonnées de données.
    arrow_sep : float
        Écartement entre les flèches d'une paire, en coordonnées de données.
    alpha : float
        Opacité maximale des flèches.
    **kwargs
        Propriétés de `.FancyArrow`, par exemple *linewidth* ou *edgecolor*.
    """

    # bloc de code
```
