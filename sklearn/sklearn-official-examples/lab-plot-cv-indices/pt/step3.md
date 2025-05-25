# Comparar Objetos de Validação Cruzada

Nesta etapa, compararemos o comportamento de validação cruzada para diferentes objetos de validação cruzada do scikit-learn. Irá percorrer vários objetos de validação cruzada comuns, visualizando o comportamento de cada um. Note como alguns utilizam as informações de grupo/classe, enquanto outros não.

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
        ["Conjunto de teste", "Conjunto de treinamento"],
        loc=(1.02, 0.8),
    )
    # Ajustar o tamanho da legenda
    plt.tight_layout()
    fig.subplots_adjust(right=0.7)
plt.show()
```
