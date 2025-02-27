# Visualiser les indices de validation croisée

Dans cette étape, nous allons définir une fonction pour visualiser le comportement de chaque objet de validation croisée. Nous effectuerons 4 partitions des données. Pour chaque partition, nous visualiserons les indices choisis pour l'ensemble d'entraînement (en bleu) et l'ensemble de test (en rouge).

```python
def plot_cv_indices(cv, X, y, group, ax, n_splits, lw=10):
    """Créer un graphique d'échantillonnage pour les indices d'un objet de validation croisée."""

    # Générer les visualisations d'entraînement/tests pour chaque partition CV
    for ii, (tr, tt) in enumerate(cv.split(X=X, y=y, groups=group)):
        # Remplir les indices avec les groupes d'entraînement/tests
        indices = np.array([np.nan] * len(X))
        indices[tt] = 1
        indices[tr] = 0

        # Visualiser les résultats
        ax.scatter(
            range(len(indices)),
            [ii + 0.5] * len(indices),
            c=indices,
            marker="_",
            lw=lw,
            cmap=cmap_cv,
            vmin=-0.2,
            vmax=1.2,
        )

    # Tracer les classes et les groupes de données à la fin
    ax.scatter(
        range(len(X)), [ii + 1.5] * len(X), c=y, marker="_", lw=lw, cmap=cmap_data
    )

    ax.scatter(
        range(len(X)), [ii + 2.5] * len(X), c=group, marker="_", lw=lw, cmap=cmap_data
    )

    # Mise en forme
    yticklabels = list(range(n_splits)) + ["classe", "groupe"]
    ax.set(
        yticks=np.arange(n_splits + 2) + 0.5,
        yticklabels=yticklabels,
        xlabel="Index d'échantillonnage",
        ylabel="Itération de validation croisée",
        ylim=[n_splits + 2.2, -0.2],
        xlim=[0, 100],
    )
    ax.set_title("{}".format(type(cv).__name__), fontsize=15)
    return ax
```
