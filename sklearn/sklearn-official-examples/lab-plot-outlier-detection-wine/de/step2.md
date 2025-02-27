# Klassifizierer und Farben definieren

Wir werden die Ausreißerdetektions-Klassifizierer definieren, die wir in diesem Lab verwenden werden. Wir werden auch die Farben definieren, die zur Darstellung der Ergebnisse verwendet werden.

```python
# Define "classifiers" to be used
classifiers = {
    "Empirical Covariance": EllipticEnvelope(support_fraction=1.0, contamination=0.25),
    "Robust Covariance (Minimum Covariance Determinant)": EllipticEnvelope(
        contamination=0.25
    ),
    "OCSVM": OneClassSVM(nu=0.25, gamma=0.35),
}
colors = ["m", "g", "b"]
```
