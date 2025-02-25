# Créez un graphique en points dispersés sur un axe polaire limité à un secteur

Nous pouvons créer un graphique en points dispersés sur un axe polaire limité à un secteur en configurant les méthodes `set_thetamin()` et `set_thetamax()` de l'objet `PolarAxes`. Nous allons définir les limites de début et de fin de theta sur `45` et `135` respectivement.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_thetamin(45)
ax.set_thetamax(135)
```
