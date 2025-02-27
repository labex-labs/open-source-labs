# Klassifizierer definieren

Wir werden zwei Klassifizierer definieren: Einen, der KNN verwendet, und einen anderen, der NCA und KNN verwendet. Wir werden Pipelines verwenden, um die Daten zu skalieren und die Klassifizierer anzuwenden.

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
