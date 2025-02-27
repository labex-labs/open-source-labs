# Définissez la fonction de tracé

Ensuite, nous définissons une fonction `plot_2d` qui trace l'ensemble de données à étiquetage multiple généré aléatoirement. Elle prend trois arguments : `n_labels`, `n_classes` et `length`.

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

Cette fonction génère l'ensemble de données en utilisant la fonction `make_multilabel_classification` avec les paramètres spécifiés. Ensuite, elle trace l'ensemble de données à l'aide de la fonction `scatter` de la bibliothèque Matplotlib. La fonction renvoie les probabilités de classe et les probabilités de caractéristique.
