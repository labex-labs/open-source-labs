# Crear una tubería y definir la cuadrícula de parámetros

Crearemos una tubería que realice la reducción de dimensionalidad seguida de una predicción con un clasificador de vectores de soporte. Usaremos reducciones de dimensionalidad no supervisadas PCA y NMF, junto con la selección de características univariada durante la búsqueda en la cuadrícula.

```python
pipe = Pipeline(
    [
        ("escalado", MinMaxScaler()),
        # la etapa reduce_dim está poblada por param_grid
        ("reduce_dim", "passthrough"),
        ("clasificar", LinearSVC(dual=False, max_iter=10000)),
    ]
)

N_FEATURES_OPTIONS = [2, 4, 8]
C_OPTIONS = [1, 10, 100, 1000]
param_grid = [
    {
        "reduce_dim": [PCA(iterated_power=7), NMF(max_iter=1_000)],
        "reduce_dim__n_components": N_FEATURES_OPTIONS,
        "clasificar__C": C_OPTIONS,
    },
    {
        "reduce_dim": [SelectKBest(mutual_info_classif)],
        "reduce_dim__k": N_FEATURES_OPTIONS,
        "clasificar__C": C_OPTIONS,
    },
]
etiquetas_reductor = ["PCA", "NMF", "KBest(mutual_info_classif)"]
```
