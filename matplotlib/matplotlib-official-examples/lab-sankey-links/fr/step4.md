# Définir la fonction `corner`

Ensuite, nous définissons la fonction `corner` qui génère un lien d'angle.

```python
def corner(sankey):
    """Génère un lien d'angle."""
    prior = len(sankey.diagrams)
    sankey.add(flows=[1, -1], orientations=[0, 1],
               patchlabel=str(prior), facecolor='k',
               prior=prior - 1, connect=(1, 0), alpha=0.5)
```
