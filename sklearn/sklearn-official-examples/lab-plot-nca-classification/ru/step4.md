# Определение классификаторов

Мы определим два классификатора: один с использованием KNN, а другой с использованием NCA и KNN. Мы будем использовать пайплайны для масштабирования данных и применения классификаторов.

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
