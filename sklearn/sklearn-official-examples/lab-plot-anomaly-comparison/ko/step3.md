# 이상 탐지 알고리즘 정의

비교할 이상 탐지 알고리즘을 정의합니다.

```python
anomaly_algorithms = [
    (
        "강건한 공분산",
        EllipticEnvelope(contamination=outliers_fraction, random_state=42),
    ),
    ("일반화된 SVM", svm.OneClassSVM(nu=outliers_fraction, kernel="rbf", gamma=0.1)),
    (
        "일반화된 SVM (SGD)",
        make_pipeline(
            Nystroem(gamma=0.1, random_state=42, n_components=150),
            SGDOneClassSVM(
                nu=outliers_fraction,
                shuffle=True,
                fit_intercept=True,
                random_state=42,
                tol=1e-6,
            ),
        ),
    ),
    (
        "격리 숲",
        IsolationForest(contamination=outliers_fraction, random_state=42),
    ),
    (
        "지역 이상치 탐지",
        LocalOutlierFactor(n_neighbors=35, contamination=outliers_fraction),
    ),
]
```
