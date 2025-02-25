# Empilement de sous-graphiques dans une direction

Pour créer plusieurs sous-graphiques empilés verticalement ou horizontalement, nous pouvons passer le nombre de lignes et de colonnes en tant qu'arguments à la fonction `subplots()`. L'objet `axs` renvoyé est un tableau numpy 1D contenant la liste des `Axes` créés.

```python
fig, axs = plt.subplots(2)
axs[0].plot(x, y)
axs[1].plot(x, -y)
```
