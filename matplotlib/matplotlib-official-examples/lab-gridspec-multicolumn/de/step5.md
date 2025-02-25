# Anpassen von Teilgrafiken

Wir können die Teilgrafiken nach Bedarf anpassen. Beispielsweise können wir den Titel der Figur mit der Funktion `fig.suptitle()` festlegen und die Achsen mit der Funktion `format_axes()` formatieren.

```python
fig.suptitle("GridSpec")

def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```
