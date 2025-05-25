# Estimar Matriz de Covariância Empírica

Neste passo, estimamos uma matriz de covariância empírica do conjunto de dados utilizando o estimador de Máxima Verossimilhança (MLE).

```python
# Estimar uma matriz de covariância empírica do conjunto de dados
emp_cov = EmpiricalCovariance().fit(X).covariance_
```
