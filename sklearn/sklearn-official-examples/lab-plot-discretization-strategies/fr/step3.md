# Appliquer différentes stratégies

Nous allons maintenant appliquer les trois différentes stratégies disponibles dans `KBinsDiscretizer` à chacun des ensembles de données. Les stratégies sont les suivantes :

- 'uniforme' : La discrétisation est uniforme pour chaque caractéristique, ce qui signifie que les largeurs de bin sont constantes dans chaque dimension.
- 'quantile' : La discrétisation est effectuée sur les valeurs quantiles, ce qui signifie que chaque bin a approximativement le même nombre d'échantillons.
- 'kmeans' : La discrétisation est basée sur les centroïdes d'une procédure de regroupement KMeans.

```python
strategies = ["uniforme", "quantile", "kmeans"]

figure = plt.figure(figsize=(14, 9))
i = 1
for ds_cnt, X in enumerate(X_list):
    ax = plt.subplot(len(X_list), len(strategies) + 1, i)
    ax.scatter(X[:, 0], X[:, 1], edgecolors="k")
    if ds_cnt == 0:
        ax.set_title("Données d'entrée", size=14)

    xx, yy = np.meshgrid(
        np.linspace(X[:, 0].min(), X[:, 0].max(), 300),
        np.linspace(X[:, 1].min(), X[:, 1].max(), 300),
    )
    grid = np.c_[xx.ravel(), yy.ravel()]

    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xticks(())
    ax.set_yticks(())

    i += 1
    # transformer l'ensemble de données avec KBinsDiscretizer
    for strategy in strategies:
        enc = KBinsDiscretizer(n_bins=4, encode="ordinal", strategy=strategy)
        enc.fit(X)
        grid_encoded = enc.transform(grid)

        ax = plt.subplot(len(X_list), len(strategies) + 1, i)

        # bandes horizontales
        horizontal = grid_encoded[:, 0].reshape(xx.shape)
        ax.contourf(xx, yy, horizontal, alpha=0.5)
        # bandes verticales
        vertical = grid_encoded[:, 1].reshape(xx.shape)
        ax.contourf(xx, yy, vertical, alpha=0.5)

        ax.scatter(X[:, 0], X[:, 1], edgecolors="k")
        ax.set_xlim(xx.min(), xx.max())
        ax.set_ylim(yy.min(), yy.max())
        ax.set_xticks(())
        ax.set_yticks(())
        if ds_cnt == 0:
            ax.set_title("stratégie='%s'" % (strategy,), size=14)

        i += 1

plt.tight_layout()
plt.show()
```
