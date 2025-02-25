# Créer une figure et un sous-graphique

Ensuite, nous devons créer une figure et un sous-graphique pour notre graphique. Nous allons utiliser le paramètre `projection` de `add_subplot` pour créer un graphique polaire.

```python
fig = plt.figure()
ax = fig.add_subplot(projection="polar", facecolor="lightgoldenrodyellow")
```
