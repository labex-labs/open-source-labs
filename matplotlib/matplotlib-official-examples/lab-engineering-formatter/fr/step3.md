# Création de la figure et des sous-graphiques

Nous devons créer une figure et des sous-graphiques pour afficher les données. Dans ce laboratoire, nous créerons deux sous-graphiques côte à côte.

```python
# Figure width is doubled (2*6.4) to display nicely 2 subplots side by side.
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(7, 9.6))
for ax in (ax0, ax1):
    ax.set_xscale('log')
```
