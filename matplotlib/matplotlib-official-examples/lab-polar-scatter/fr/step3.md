# Créez un graphique en points dispersés sur un axe polaire

Nous allons créer un graphique en points dispersés sur un axe polaire à l'aide de la fonction `plt.scatter()`. Nous allons définir le paramètre `projection` sur `'polar'` et passer les valeurs de rayon, d'angle, de couleur et d'aire en tant que paramètres.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
```
