# Définir des classifieurs

Nous allons définir deux classifieurs : l'un utilisant le KNN et l'autre utilisant l'NCA et le KNN. Nous utiliserons des pipelines pour mettre à l'échelle les données et appliquer les classifieurs.

```python
names = ["KNN", "NCA, KNN"]

classifiers = [
    Pipeline(
        [
            ("scaler", StandardScaler()),
            ("knn", KNeighborsClassifier(n_neighbors=n_neighbors)),
        ]
    ),
    Pipeline(
        [
            ("scaler", StandardScaler()),
            ("nca", NeighborhoodComponentsAnalysis()),
            ("knn", KNeighborsClassifier(n_neighbors=n_neighbors)),
        ]
    ),
]
```
