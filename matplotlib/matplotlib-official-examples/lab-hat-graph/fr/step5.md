# Code complet

Voici le code complet pour créer le graphique en chapeau en Python.

```python
import matplotlib.pyplot as plt
import numpy as np


def hat_graph(ax, xlabels, values, group_labels):
    """
    Crée un graphique en chapeau.

    Paramètres
    ----------
    ax : matplotlib.axes.Axes
        Les axes sur lesquels tracer.
    xlabels : liste de str
        Les noms des catégories à afficher sur l'axe des x.
    values : (M, N) array-like
        Les valeurs des données.
        Les lignes sont les groupes (len(group_labels) == M).
        Les colonnes sont les catégories (len(xlabels) == N).
    group_labels : liste de str
        Les étiquettes des groupes affichées dans la légende.
    """

    def label_bars(heights, rects):
        """Attache une étiquette de texte au-dessus de chaque barre."""
        for height, rect in zip(heights, rects):
            ax.annotate(f'{height}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 4),  # Décalage vertical de 4 points.
                        textcoords='offset points',
                        ha='center', va='bottom')

    values = np.asarray(values)
    x = np.arange(values.shape[1])
    ax.set_xticks(x, labels=xlabels)
    spacing = 0.3  # Espacement entre les groupes de chapeaux
    width = (1 - spacing) / values.shape[0]
    heights0 = values[0]
    for i, (heights, group_label) in enumerate(zip(values, group_labels)):
        style = {'fill': False} if i == 0 else {'edgecolor': 'black'}
        rects = ax.bar(x - spacing/2 + i * width, heights - heights0,
                       width, bottom=heights0, label=group_label, **style)
        label_bars(heights, rects)


# initialise labels and a numpy array make sure you have
# N labels of N number of values in the array
xlabels = ['I', 'II', 'III', 'IV', 'V']
playerA = np.array([5, 15, 22, 20, 25])
playerB = np.array([25, 32, 34, 30, 27])

fig, ax = plt.subplots()
hat_graph(ax, xlabels, [playerA, playerB], ['Player A', 'Player B'])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Games')
ax.set_ylabel('Score')
ax.set_ylim(0, 60)
ax.set_title('Scores by number of game and players')
ax.legend()

fig.tight_layout()
plt.show()
```
