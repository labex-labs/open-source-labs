# Das Diagramm einrichten

Als nächstes werden wir das Diagramm einrichten, indem wir eine Figur und ein Array von Teildiagrammen erstellen. Wir definieren auch eine `setup`-Funktion, die die gemeinsamen Parameter für die Achsen im Beispiel einstellt.

```python
fig, axs = plt.subplots(8, 1, figsize=(8, 6))

def setup(ax, title):
    """Set up common parameters for the Axes in the example."""
    # only show the bottom spine
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines[['left', 'right', 'top']].set_visible(False)

    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.text(0.0, 0.2, title, transform=ax.transAxes,
            fontsize=14, fontname='Monospace', color='tab:blue')
```
