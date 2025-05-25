# 분류기 정의

KNN 을 사용하는 분류기와 NCA 및 KNN 을 사용하는 분류기를 정의합니다. 파이프라인을 사용하여 데이터를 스케일링하고 분류기를 적용합니다.

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
