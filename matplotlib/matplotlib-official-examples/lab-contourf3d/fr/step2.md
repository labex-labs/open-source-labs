# Créez les objets Figure et Axes

Nous allons maintenant créer les objets Figure et Axes en utilisant la méthode `add_subplot()`. Nous définirons le paramètre `projection` sur `'3d'` pour créer un tracé 3D.

```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
```
