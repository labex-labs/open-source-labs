# Erstellen eines Balkendiagramms im xkcd-Stil

In diesem Schritt werden wir ein Balkendiagramm im xkcd-Stil erstellen. Das Diagramm basiert auf der Comicserie "The Data So Far" von XKCD.

```python
with plt.xkcd():
    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.bar([0, 1], [0, 100], 0.25)
    ax.spines[['top', 'right']].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['BESTÄTIGT DURCH\nEXPERIMENT', 'WIDERLEGT DURCH\nEXPERIMENT'])
    ax.set_xlim([-0.5, 1.5])
    ax.set_yticks([])
    ax.set_ylim([0, 110])

    ax.set_title("BEHARTIGUNGEN VON ÜBER NATÜRLICHEN KRÄFTEN")

    fig.text(
        0.5, 0.05,
        '"The Data So Far" from xkcd by Randall Munroe',
        ha='center')

plt.show()
```
