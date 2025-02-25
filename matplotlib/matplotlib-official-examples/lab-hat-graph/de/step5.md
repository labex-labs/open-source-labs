# Vollständiger Code

Hier ist der vollständige Code in Python, um den Hut-Graphen zu erstellen.

```python
import matplotlib.pyplot as plt
import numpy as np


def hat_graph(ax, xlabels, values, group_labels):
    """
    Erstellt einen Hut-Graphen.

    Parameter
    ----------
    ax : matplotlib.axes.Axes
        Die Achsen, in die geplottet werden soll.
    xlabels : Liste von str
        Die Kategorie-Namen, die auf der x-Achse angezeigt werden sollen.
    values : (M, N) array-ähnlich
        Die Datenwerte.
        Die Zeilen sind die Gruppen (len(group_labels) == M).
        Die Spalten sind die Kategorien (len(xlabels) == N).
    group_labels : Liste von str
        Die Gruppennamen, die in der Legende angezeigt werden.
    """

    def label_bars(heights, rects):
        """Fügt eine Textbeschriftung über jeder Bar hinzu."""
        for height, rect in zip(heights, rects):
            ax.annotate(f'{height}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 4),  # 4 Punkte vertikaler Abstand.
                        textcoords='offset points',
                        ha='center', va='bottom')

    values = np.asarray(values)
    x = np.arange(values.shape[1])
    ax.set_xticks(x, labels=xlabels)
    spacing = 0.3  # Abstand zwischen den Hut-Gruppen
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
ax.set_xlabel('Spiele')
ax.set_ylabel('Punkte')
ax.set_ylim(0, 60)
ax.set_title('Punkte nach Anzahl von Spielen und Spielern')
ax.legend()

fig.tight_layout()
plt.show()
```
