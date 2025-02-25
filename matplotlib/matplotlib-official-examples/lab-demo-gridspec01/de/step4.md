# Achsen annotieren

Um die Achsen zu annotieren, können wir durch die Achsen der Figur iterieren und Text hinzufügen, indem wir die `text`-Funktion verwenden, und die `tick_params`-Funktion verwenden, um die Tick-Labels zu entfernen.

```python
def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)
```
