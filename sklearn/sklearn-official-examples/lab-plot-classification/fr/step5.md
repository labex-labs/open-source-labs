# Visualiser les limites de décision

Nous allons parcourir deux valeurs différentes de poids, "uniforme" et "distance", et tracer les limites de décision pour chaque valeur de poids. Nous utiliserons la classe `KNeighborsClassifier` du module `neighbors` pour effectuer la classification.

```python
n_neighbors = 15

for weights in ["uniform", "distance"]:
    # créer une instance du classifieur Neighbours et ajuster les données
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

    # tracer les limites de décision
    _, ax = plt.subplots()
    DecisionBoundaryDisplay.from_estimator(
        clf,
        X,
        cmap=cmap_light,
        ax=ax,
        response_method="predict",
        plot_method="pcolormesh",
        xlabel=iris.feature_names[0],
        ylabel=iris.feature_names[1],
        shading="auto",
    )

    # tracer les points d'entraînement
    sns.scatterplot(
        x=X[:, 0],
        y=X[:, 1],
        hue=iris.target_names[y],
        palette=cmap_bold,
        alpha=1.0,
        edgecolor="black",
    )
    plt.title(
        "Classification à 3 classes (k = %i, poids = '%s')" % (n_neighbors, weights)
    )

plt.show()
```
