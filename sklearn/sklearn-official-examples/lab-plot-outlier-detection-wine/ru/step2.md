# Определяем классификаторы и цвета

Мы определим классификаторы обнаружения выбросов, которые будем использовать в этом практическом занятии. Также определим цвета, которые будут использоваться для построения графиков результатов.

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
