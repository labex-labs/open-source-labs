# Definir Algoritmos de Detecção de Anomalias

Defina os algoritmos de detecção de anomalias a serem comparados.

```python
anomaly_algorithms = [
    (
        "Covariância Robusta",
        EllipticEnvelope(contamination=outliers_fraction, random_state=42),
    ),
    ("SVM de Uma Classe", svm.OneClassSVM(nu=outliers_fraction, kernel="rbf", gamma=0.1)),
    (
        "SVM de Uma Classe (SGD)",
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
        "Floresta de Isolamento",
        IsolationForest(contamination=outliers_fraction, random_state=42),
    ),
    (
        "Fator Local de Desvio",
        LocalOutlierFactor(n_neighbors=35, contamination=outliers_fraction),
    ),
]
```
