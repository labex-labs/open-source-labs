# Visualiser les poids

Enfin, nous allons visualiser les poids de la première couche du MLP. Nous allons créer une grille de sous-graphiques 4x4 et afficher chaque poids sous forme d'une image en niveaux de gris de 28x28 pixels.

```python
fig, axes = plt.subplots(4, 4)
vmin, vmax = mlp.coefs_[0].min(), mlp.coefs_[0].max()
for coef, ax in zip(mlp.coefs_[0].T, axes.ravel()):
    ax.matshow(coef.reshape(28, 28), cmap=plt.cm.gray, vmin=0.5 * vmin, vmax=0.5 * vmax)
    ax.set_xticks(())
    ax.set_yticks(())

plt.show()
```
