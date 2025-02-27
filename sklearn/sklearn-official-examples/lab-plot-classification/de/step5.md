# Visualisieren der Entscheidungsgrenzen

Wir werden in einer Schleife durch zwei verschiedene Gewichts-Werte, "uniform" und "distance", iterieren und die Entscheidungsgrenzen für jeden Gewichts-Wert darstellen. Wir werden die Klasse `KNeighborsClassifier` aus dem Modul `neighbors` verwenden, um die Klassifizierung durchzuführen.

```python
n_neighbors = 15

for weights in ["uniform", "distance"]:
    # create an instance of Neighbours Classifier and fit the data
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

    # plot the decision boundaries
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

    # plot the training points
    sns.scatterplot(
        x=X[:, 0],
        y=X[:, 1],
        hue=iris.target_names[y],
        palette=cmap_bold,
        alpha=1.0,
        edgecolor="black",
    )
    plt.title(
        "3-Class classification (k = %i, weights = '%s')" % (n_neighbors, weights)
    )

plt.show()
```
