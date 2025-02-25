# Créez un graphique à points

Dans cette étape, nous allons créer un graphique à points à l'aide des données aléatoires de l'Étape 2.

```python
fig, ax = plt.subplots(figsize=(5.5, 5.5))
ax.scatter(x, y)
ax.set_aspect(1.)
```
