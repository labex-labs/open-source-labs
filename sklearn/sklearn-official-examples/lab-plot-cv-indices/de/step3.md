# Vergleiche Kreuzvalidierungsobjekte

In diesem Schritt werden wir das Kreuzvalidierungsverhalten für verschiedene scikit-learn-Kreuzvalidierungsobjekte vergleichen. Wir werden durch mehrere übliche Kreuzvalidierungsobjekte iterieren und das Verhalten jedes visualisieren. Beachten Sie, wie einige die Gruppierungs-/Klasseninformation verwenden, während andere dies nicht tun.

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
        ["Testing set", "Training set"],
        loc=(1.02, 0.8),
    )
    # Make the legend fit
    plt.tight_layout()
    fig.subplots_adjust(right=0.7)
plt.show()
```

# Vergleiche Kreuzvalidierungsobjekte

In diesem Schritt werden wir das Kreuzvalidierungsverhalten für verschiedene scikit-learn-Kreuzvalidierungsobjekte vergleichen. Wir werden durch mehrere übliche Kreuzvalidierungsobjekte iterieren und das Verhalten jedes visualisieren. Beachten Sie, wie einige die Gruppierungs-/Klasseninformation verwenden, während andere dies nicht tun.

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
        ["Testing set", "Training set"],
        loc=(1.02, 0.8),
    )
    # Mach die Legende passen
    plt.tight_layout()
    fig.subplots_adjust(right=0.7)
plt.show()
```
