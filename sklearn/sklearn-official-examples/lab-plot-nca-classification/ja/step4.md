# 分類器の定義

2 つの分類器を定義します。1 つは KNN を使用し、もう 1 つは NCA と KNN を使用します。データをスケーリングして分類器を適用するためにパイプラインを使用します。

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
