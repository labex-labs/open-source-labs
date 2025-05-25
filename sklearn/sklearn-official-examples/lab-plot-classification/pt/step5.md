# Visualizar as fronteiras de decisão

Iremos percorrer dois valores diferentes de peso, "uniforme" e "distância", e plotar as fronteiras de decisão para cada valor de peso. Usaremos a classe `KNeighborsClassifier` do módulo `neighbors` para realizar a classificação.

```python
n_neighbors = 15

for weights in ["uniform", "distance"]:
    # criar uma instância de Neighbours Classifier e ajustar os dados
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

    # plotar as fronteiras de decisão
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

    # plotar os pontos de treinamento
    sns.scatterplot(
        x=X[:, 0],
        y=X[:, 1],
        hue=iris.target_names[y],
        palette=cmap_bold,
        alpha=1.0,
        edgecolor="black",
    )
    plt.title(
        "Classificação de 3 classes (k = %i, pesos = '%s')" % (n_neighbors, weights)
    )

plt.show()
```
