# Achsen formatieren

Wir werden die Achsen aller Teilplots mit der Funktion `format_axes` formatieren. Diese Funktion fügt jeder Teilgrafik eine Textbeschriftung hinzu und entfernt die Skalenmarkierungen.

```python
def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```
