# Visualizar los límites de decisión

Recorreremos dos valores diferentes de peso, "uniforme" y "distancia", y graficaremos los límites de decisión para cada valor de peso. Usaremos la clase `KNeighborsClassifier` del módulo `neighbors` para realizar la clasificación.

```python
n_neighbors = 15

for weights in ["uniforme", "distancia"]:
    # crear una instancia del clasificador de vecinos y ajustar los datos
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

    # graficar los límites de decisión
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

    # graficar los puntos de entrenamiento
    sns.scatterplot(
        x=X[:, 0],
        y=X[:, 1],
        hue=iris.target_names[y],
        palette=cmap_bold,
        alpha=1.0,
        edgecolor="black",
    )
    plt.title(
        "Clasificación de 3 clases (k = %i, pesos = '%s')" % (n_neighbors, weights)
    )

plt.show()
```
