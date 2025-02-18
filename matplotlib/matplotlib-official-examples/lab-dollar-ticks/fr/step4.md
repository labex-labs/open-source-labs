# Personnalisation des paramètres des graduations

Nous pouvons également personnaliser les paramètres des graduations (ticks) pour ajuster davantage l'apparence de notre graphique. Dans cet exemple, nous allons changer la couleur des étiquettes des graduations en vert et les déplacer du côté droit du graphique.

```python
# Customize tick parameters
ax.tick_params(axis='y', which='major', labelcolor='green', labelright=True)
```

Dans le code ci-dessus, nous utilisons la méthode `tick_params` pour personnaliser les paramètres des graduations de l'axe des ordonnées (y-axis). Nous définissons le paramètre `axis` sur `'y'` pour spécifier que nous personnalisons l'axe des ordonnées, et le paramètre `which` sur `'major'` pour spécifier que nous personnalisons les graduations principales. Nous définissons le paramètre `labelcolor` sur `'green'` pour changer la couleur des étiquettes des graduations, et le paramètre `labelright` sur `True` pour déplacer les étiquettes des graduations du côté droit du graphique.
