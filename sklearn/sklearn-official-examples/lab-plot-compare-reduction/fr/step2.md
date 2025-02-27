# Créez un pipeline et définissez la grille de paramètres

Nous allons créer un pipeline qui effectue une réduction de dimensionnalité suivie d'une prédiction avec un classifieur à vecteurs de support. Nous utiliserons des réductions de dimensionnalité non supervisées PCA et NMF, ainsi qu'une sélection de caractéristiques univariée lors de la recherche en grille.

```python
pipe = Pipeline(
    [
        ("scaling", MinMaxScaler()),
        # l'étape reduce_dim est remplie par param_grid
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
