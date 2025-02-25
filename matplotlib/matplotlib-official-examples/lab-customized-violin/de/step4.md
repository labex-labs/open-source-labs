# Stil der Achsen festlegen

Schließlich werden wir den Stil der x-Achse durch Angabe der Strichmarkenbeschriftungen und -grenzen festlegen. Dazu definieren wir eine Hilfsfunktion `set_axis_style`.

```python
# set style for the axes
labels = ['A', 'B', 'C', 'D']
set_axis_style(ax2, labels)

def set_axis_style(ax, labels):
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlim(0.25, len(labels) + 0.75)
    ax.set_xlabel('Sample Name')
```
