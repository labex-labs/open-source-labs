# Créez un graphique en points dispersés sur un axe polaire avec origine décalée

Nous pouvons créer un graphique en points dispersés sur un axe polaire avec une origine décalée en configurant les méthodes `set_rorigin()` et `set_theta_zero_location()` de l'objet `PolarAxes`. Nous allons définir le rayon d'origine sur `-2,5` et l'emplacement du zéro de theta sur `'W'` avec un décalage de `10`.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_rorigin(-2.5)
ax.set_theta_zero_location('W', offset=10)
```
