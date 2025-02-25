# Création d'un graphique

Pour créer un graphique, nous devons tout d'abord définir les données que nous souhaitons tracer. Dans cet exemple, nous utiliserons la bibliothèque `numpy` pour générer des données d'échantillonnage.

```python
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x)
```

Ensuite, nous créons une nouvelle figure et un nouvel axe en utilisant `plt.subplots()`. Nous définirons les limites x et y du graphique puis tracerons les données en utilisant `plot()`.

```python
fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([-1.2, 1.2])
ax.plot(x, y)
```
