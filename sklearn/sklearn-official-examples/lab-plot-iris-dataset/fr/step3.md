# Visualiser les données

Nous allons visualiser le Jeu de données Iris à l'aide d'un graphique à points dispersés. Nous allons tracer la Longueur du sépale en fonction de la Largeur du sépale, et colorer les points selon leur classe.

```python
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor="k")
plt.xlabel("Longueur du sépale")
plt.ylabel("Largeur du sépale")

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
```
