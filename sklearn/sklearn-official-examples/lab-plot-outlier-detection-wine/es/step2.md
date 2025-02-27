# Definir clasificadores y colores

Definiremos los clasificadores de detección de valores atípicos que utilizaremos en este laboratorio. También definiremos los colores que se utilizarán para graficar los resultados.

```python
# Definir los "clasificadores" que se utilizarán
classifiers = {
    "Empirical Covariance": EllipticEnvelope(support_fraction=1.0, contamination=0.25),
    "Robust Covariance (Minimum Covariance Determinant)": EllipticEnvelope(
        contamination=0.25
    ),
    "OCSVM": OneClassSVM(nu=0.25, gamma=0.35),
}
colors = ["m", "g", "b"]
```
