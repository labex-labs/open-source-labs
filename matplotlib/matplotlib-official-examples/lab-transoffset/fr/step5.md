# Création d'un graphique polaire

Nous allons maintenant créer un graphique polaire à l'aide de la fonction `polar` de `matplotlib.pyplot`.

```python
ax = plt.subplot(2, 1, 2, projection='polar')

# Plot the data
for x, y in zip(xs, ys):
    plt.polar(x, y, 'ro')
```
