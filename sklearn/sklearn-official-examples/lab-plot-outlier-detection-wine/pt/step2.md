# Definir classificadores e cores

Vamos definir os classificadores de deteção de valores discrepantes que usaremos neste laboratório. Também definiremos as cores que serão usadas para representar os resultados.

```python
# Definir "classificadores" a serem usados
classifiers = {
    "Covariância Empírica": EllipticEnvelope(support_fraction=1.0, contamination=0.25),
    "Covariância Robusta (Determinante de Covariância Mínima)": EllipticEnvelope(
        contamination=0.25
    ),
    "OCSVM": OneClassSVM(nu=0.25, gamma=0.35),
}
colors = ["m", "g", "b"]
```
