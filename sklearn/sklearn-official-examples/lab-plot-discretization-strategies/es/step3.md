# Aplicar diferentes estrategias

Ahora aplicaremos las tres diferentes estrategias disponibles en `KBinsDiscretizer` a cada uno de los conjuntos de datos. Las estrategias son:

- 'uniforme': La discretización es uniforme en cada característica, lo que significa que los anchos de los intervalos son constantes en cada dimensión.
- 'cuantílica': La discretización se realiza en los valores cuantilados, lo que significa que cada intervalo tiene aproximadamente el mismo número de muestras.
- 'kmeans': La discretización se basa en los centroides de un procedimiento de agrupamiento KMeans.

```python
strategies = ["uniform", "quantile", "kmeans"]

figure = plt.figure(figsize=(14, 9))
i = 1
for ds_cnt, X in enumerate(X_list):
    ax = plt.subplot(len(X_list), len(strategies) + 1, i)
    ax.scatter(X[:, 0], X[:, 1], edgecolors="k")
    if ds_cnt == 0:
        ax.set_title("Datos de entrada", size=14)

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
    # transformar el conjunto de datos con KBinsDiscretizer
    for strategy in strategies:
        enc = KBinsDiscretizer(n_bins=4, encode="ordinal", strategy=strategy)
        enc.fit(X)
        grid_encoded = enc.transform(grid)

        ax = plt.subplot(len(X_list), len(strategies) + 1, i)

        # rayas horizontales
        horizontal = grid_encoded[:, 0].reshape(xx.shape)
        ax.contourf(xx, yy, horizontal, alpha=0.5)
        # rayas verticales
        vertical = grid_encoded[:, 1].reshape(xx.shape)
        ax.contourf(xx, yy, vertical, alpha=0.5)

        ax.scatter(X[:, 0], X[:, 1], edgecolors="k")
        ax.set_xlim(xx.min(), xx.max())
        ax.set_ylim(yy.min(), yy.max())
        ax.set_xticks(())
        ax.set_yticks(())
        if ds_cnt == 0:
            ax.set_title("estrategia='%s'" % (strategy,), size=14)

        i += 1

plt.tight_layout()
plt.show()
```
