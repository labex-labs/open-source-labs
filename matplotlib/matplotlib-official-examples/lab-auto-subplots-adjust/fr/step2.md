# Créez le graphique

Créeons un graphique linéaire simple avec quelques étiquettes de l'axe des ordonnées longues.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.set_yticks([2, 5, 7], labels=['really, really, really', 'long', 'labels'])
```
