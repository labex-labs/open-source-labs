# Estimer la matrice de covariance empirique

Dans cette étape, nous estimons une matrice de covariance empirique de l'ensemble de données en utilisant l'estimateur Maximum Likelihood Estimate (MLE).

```python
# Estimate an empirical covariance matrix of the dataset
emp_cov = EmpiricalCovariance().fit(X).covariance_
```
