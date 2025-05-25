# Criar um pipeline e definir a grade de parâmetros

Criaremos um pipeline que realiza redução de dimensionalidade seguida de previsão com um classificador de vetores de suporte. Usaremos reduções de dimensionalidade não supervisionadas PCA e NMF, juntamente com seleção de recursos univariada durante a busca na grade.

```python
pipe = Pipeline(
    [
        ("scaling", MinMaxScaler()),
        # o estágio reduce_dim é preenchido pelo param_grid
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
