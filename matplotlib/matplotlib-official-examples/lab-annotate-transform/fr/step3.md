# Création du graphique

Maintenant, nous allons créer le graphique en utilisant la bibliothèque `matplotlib.pyplot`. Nous allons définir les limites des axes x et y puis tracer les données.

```python
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
```
