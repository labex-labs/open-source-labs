# Création d'un nuage de points

Nous allons maintenant créer un nuage de points à l'aide de la fonction `plot` de `matplotlib.pyplot`.

```python
fig = plt.figure(figsize=(5, 10))
ax = plt.subplot(2, 1, 1)

# Plot the data
for x, y in zip(xs, ys):
    plt.plot(x, y, 'ro')
```
