# Afficher les limites de décision sur le graphique de dispersion

Nous allons afficher les limites de décision sur le graphique de dispersion en utilisant DecisionBoundaryDisplay de la bibliothèque scikit-learn.

```python
_, ax = plt.subplots(figsize=(4, 3))
DecisionBoundaryDisplay.from_estimator(
    logreg,
    X,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    plot_method="pcolormesh",
    shading="auto",
    xlabel="Longueur du sépale",
    ylabel="Largeur du sépale",
    eps=0.5,
)

# Tracer également les points d'entraînement
plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors="k", cmap=plt.cm.Paired)

plt.xticks(())
plt.yticks(())

plt.show()
```
