# Definir la función de trazado

A continuación, definimos una función `plot_2d` que traza el conjunto de datos de múltiples etiquetas generado aleatoriamente. Toma tres argumentos: `n_labels`, `n_classes` y `length`.

```python
def plot_2d(ax, n_labels=1, n_classes=3, length=50):
    X, Y, p_c, p_w_c = make_ml_clf(
        n_samples=150,
        n_features=2,
        n_classes=n_classes,
        n_labels=n_labels,
        length=length,
        allow_unlabeled=False,
        return_distributions=True,
        random_state=RANDOM_SEED,
    )

    ax.scatter(
        X[:, 0], X[:, 1], color=COLORS.take((Y * [1, 2, 4]).sum(axis=1)), marker="."
    )
    ax.scatter(
        p_w_c[0] * length,
        p_w_c[1] * length,
        marker="*",
        linewidth=0.5,
        edgecolor="black",
        s=20 + 1500 * p_c**2,
        color=COLORS.take([1, 2, 4]),
    )
    ax.set_xlabel("Feature 0 count")
    return p_c, p_w_c
```

Esta función genera el conjunto de datos utilizando la función `make_multilabel_classification` con los parámetros especificados. Luego, traza el conjunto de datos utilizando la función `scatter` de la biblioteca Matplotlib. La función devuelve las probabilidades de clase y las probabilidades de características.
