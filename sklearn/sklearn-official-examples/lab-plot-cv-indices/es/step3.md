# Comparar objetos de validación cruzada

En este paso, compararemos el comportamiento de la validación cruzada para diferentes objetos de validación cruzada de scikit-learn. Recorreremos varios objetos comunes de validación cruzada, visualizando el comportamiento de cada uno. Observe cómo algunos utilizan la información de grupo/clase mientras que otros no.

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
        ["Conjunto de prueba", "Conjunto de entrenamiento"],
        loc=(1.02, 0.8),
    )
    # Hacer que la leyenda quepa
    plt.tight_layout()
    fig.subplots_adjust(right=0.7)
plt.show()
```

# Comparar objetos de validación cruzada

En este paso, compararemos el comportamiento de la validación cruzada para diferentes objetos de validación cruzada de scikit-learn. Recorreremos varios objetos comunes de validación cruzada, visualizando el comportamiento de cada uno. Observe cómo algunos utilizan la información de grupo/clase mientras que otros no.

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

Para cada cv en cvs:
    this_cv = cv(n_splits=n_splits)
    fig, ax = plt.subplots(figsize=(6, 3))
    plot_cv_indices(this_cv, X, y, groups, ax, n_splits)

    ax.legend(
        [Patch(color=cmap_cv(0.8)), Patch(color=cmap_cv(0.02))],
        ["Conjunto de prueba", "Conjunto de entrenamiento"],
        loc=(1.02, 0.8),
    )
    # Hacer que la leyenda quepa
    plt.tight_layout()
    fig.subplots_adjust(right=0.7)
plt.show()
```
