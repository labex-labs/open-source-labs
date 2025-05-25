# Ajustar Estimadores de Covariância MCD e MLE aos Dados

Ajustaremos os estimadores de covariância baseados em MCD e MLE aos nossos dados e imprimiremos as matrizes de covariância estimadas. Note que a variância estimada da característica 2 é muito maior com o estimador baseado em MLE (7,5) do que com o estimador robusto MCD (1,2). Isto demonstra que o estimador robusto baseado em MCD é muito mais resistente às amostras de valores discrepantes, que foram concebidas para ter uma variância muito maior na característica 2.

```python
from sklearn.covariance import EmpiricalCovariance, MinCovDet

# ajustar um estimador robusto MCD aos dados
robust_cov = MinCovDet().fit(X)
# ajustar um estimador MLE aos dados
emp_cov = EmpiricalCovariance().fit(X)
print(
    "Matriz de covariância estimada:\nMCD (Robusto):\n{}\nMLE:\n{}".format(
        robust_cov.covariance_, emp_cov.covariance_
    )
)
```
