# Définir les classifieurs et les couleurs

Nous allons définir les classifieurs de détection d'anomalies que nous utiliserons dans ce laboratoire. Nous allons également définir les couleurs qui seront utilisées pour tracer les résultats.

```python
# Définir les "classifieurs" à utiliser
classifiers = {
    "Empirical Covariance": EllipticEnvelope(support_fraction=1.0, contamination=0.25),
    "Robust Covariance (Minimum Covariance Determinant)": EllipticEnvelope(
        contamination=0.25
    ),
    "OCSVM": OneClassSVM(nu=0.25, gamma=0.35),
}
colors = ["m", "g", "b"]
```
