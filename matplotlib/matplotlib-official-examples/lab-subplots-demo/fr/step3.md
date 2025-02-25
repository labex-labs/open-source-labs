# Empilement de sous-graphiques dans deux directions

Pour créer une grille de sous-graphiques, nous pouvons passer le nombre de lignes et de colonnes en tant qu'arguments à la fonction `subplots()`. L'objet `axs` renvoyé est un tableau NumPy 2D.

```python
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].plot(x, y, 'tab:orange')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 1].plot(x, -y, 'tab:red')
```
