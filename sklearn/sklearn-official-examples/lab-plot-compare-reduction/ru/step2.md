# Создаем конвейер и определяем сетку параметров

Создадим конвейер, который будет выполнять уменьшение размерности, за которым следует предсказание с использованием классификатора на основе векторов поддержки. Будем использовать методы безнадзорной уменьшения размерности PCA и NMF, а также отбор признаков с использованием одномерной статистики в ходе сеточного поиска.

```python
pipe = Pipeline(
    [
        ("scaling", MinMaxScaler()),
        # этап reduce_dim заполняется param_grid
        ("reduce_dim", "passthrough"),
        ("classify", LinearSVC(dual=False, max_iter=10000)),
    ]
)

N_FEATURES_OPTIONS = [2, 4, 8]
C_OPTIONS = [1, 10, 100, 1000]
param_grid = [
    {
        "reduce_dim": [PCA(iterated_power=7), NMF(max_iter=1_000)],
        "reduce_dim__n_components": N_FEATURES_OPTIONS,
        "classify__C": C_OPTIONS,
    },
    {
        "reduce_dim": [SelectKBest(mutual_info_classif)],
        "reduce_dim__k": N_FEATURES_OPTIONS,
        "classify__C": C_OPTIONS,
    },
]
reducer_labels = ["PCA", "NMF", "KBest(mutual_info_classif)"]
```
