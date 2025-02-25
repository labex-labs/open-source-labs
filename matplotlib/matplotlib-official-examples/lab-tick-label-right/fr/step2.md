# Définir les étiquettes d'échelonnement par défaut de l'axe des y sur le côté droit

Nous pouvons définir les étiquettes d'échelonnement par défaut de l'axe des y sur le côté droit du graphique à l'aide du code suivant :

```python
plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
plt.rcParams['ytick.left'] = plt.rcParams['ytick.labelleft'] = False
```
