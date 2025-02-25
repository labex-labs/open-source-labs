# Definieren der `corner`-Funktion

Als nächstes definieren wir die `corner`-Funktion, die einen Eckverbindungsstrang generiert.

```python
def corner(sankey):
    """Generate a corner link."""
    prior = len(sankey.diagrams)
    sankey.add(flows=[1, -1], orientations=[0, 1],
               patchlabel=str(prior), facecolor='k',
               prior=prior - 1, connect=(1, 0), alpha=0.5)
```
