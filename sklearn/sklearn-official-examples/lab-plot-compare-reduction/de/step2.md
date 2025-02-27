# Erstellen eines Pipelines und Definieren eines Parameter-Grids

Wir werden eine Pipeline erstellen, die zunächst eine Dimensionsreduzierung durchführt und anschließend mit einem Support-Vektor-Klassifizierer eine Vorhersage macht. Wir werden uns auf die unsupervised PCA- und NMF-Dimensionsreduzierungen stützen und zusätzlich eine einvariate Merkmalsauswahl während der Grid-Suche durchführen.

```python
pipe = Pipeline(
    [
        ("scaling", MinMaxScaler()),
        # der reduce_dim-Schritt wird durch das param_grid befüllt
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
