# Comparer les objets de validation croisée

Dans cette étape, nous allons comparer le comportement de la validation croisée pour différents objets de validation croisée de scikit-learn. Nous allons parcourir plusieurs objets de validation croisée courants, en visualisant le comportement de chacun. Notez comment certains utilisent les informations de groupe/classe tandis que d'autres ne le font pas.

```python
cvs = [
    KFold,
    GroupKFold,
    ShuffleSplit,
    StratifiedKFold,
    StratifiedGroupKFold,
    GroupShuffleSplit,
    StratifiedShuffleSplit,
    TimeSeriesSplit,
]

for cv in cvs:
    this_cv = cv(n_splits=n_splits)
    fig, ax = plt.subplots(figsize=(6, 3))
    plot_cv_indices(this_cv, X, y, groups, ax, n_splits)

    ax.legend(
        [Patch(color=cmap_cv(0.8)), Patch(color=cmap_cv(0.02))],
        ["Ensemble de test", "Ensemble d'entraînement"],
        loc=(1.02, 0.8),
    )
    # Ajuster la légende pour qu'elle rentre
    plt.tight_layout()
    fig.subplots_adjust(right=0.7)
plt.show()
```
