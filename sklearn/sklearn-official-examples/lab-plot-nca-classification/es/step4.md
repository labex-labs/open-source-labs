# Definir clasificadores

Definiremos dos clasificadores: uno que utiliza KNN y otro que utiliza NCA y KNN. Utilizaremos tuberías para escalar los datos y aplicar los clasificadores.

```python
names = ["KNN", "NCA, KNN"]

classifiers = [
    Pipeline(
        [
            ("escalador", StandardScaler()),
            ("knn", KNeighborsClassifier(n_neighbors=n_neighbors)),
        ]
    ),
    Pipeline(
        [
            ("escalador", StandardScaler()),
            ("nca", NeighborhoodComponentsAnalysis()),
            ("knn", KNeighborsClassifier(n_neighbors=n_neighbors)),
        ]
    ),
]
```
