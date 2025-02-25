# Die Funktion für den Hut-Graphen definieren

In diesem Schritt werden wir eine Funktion definieren, die den Hut-Graphen erstellt. Die Funktion nimmt die folgenden Parameter entgegen:

- ax: Die Achsen, in die geplottet werden soll.
- xlabels: Die Kategorie-Namen, die auf der x-Achse angezeigt werden sollen.
- values: Die Datenwerte. Die Zeilen sind die Gruppen, und die Spalten sind die Kategorien.
- group_labels: Die Gruppennamen, die in der Legende angezeigt werden.

```python
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
```
