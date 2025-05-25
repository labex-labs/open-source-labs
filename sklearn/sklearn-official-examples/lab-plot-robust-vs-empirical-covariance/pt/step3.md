# Estimar Matriz de Covariância Robusta

Neste passo, estimamos uma matriz de covariância robusta do conjunto de dados utilizando o estimador Minimum Covariance Determinant (MCD).

```python
# Estimar uma matriz de covariância robusta do conjunto de dados
mcd = MinCovDet().fit(X)
robust_cov = mcd.covariance_
```
