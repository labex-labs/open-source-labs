# Configurer la représentation graphique

Maintenant, nous pouvons configurer la représentation graphique. Nous allons utiliser `plt.subplots()` pour créer un objet figure et un objet axe. Ensuite, nous utiliserons `ax.triplot()` pour tracer la triangulation.

```python
fig, ax = plt.subplots()
ax.triplot(triang)
```
