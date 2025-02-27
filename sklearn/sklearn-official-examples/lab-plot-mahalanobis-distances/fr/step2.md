# Ajuster les estimateurs de covariance MCD et MLE aux données

Nous ajusterons les estimateurs de covariance basés sur MCD et MLE à nos données et afficherons les matrices de covariance estimées. Remarquez que la variance estimée de la caractéristique 2 est beaucoup plus élevée avec l'estimateur basé sur MLE (7,5) que celle de l'estimateur robuste MCD (1,2). Cela montre que l'estimateur robuste basé sur MCD est beaucoup plus résistant aux échantillons aberrants, qui ont été conçus pour avoir une variance beaucoup plus élevée dans la caractéristique 2.

```python
from sklearn.covariance import EmpiricalCovariance, MinCovDet

# fit a MCD robust estimator to data
robust_cov = MinCovDet().fit(X)
# fit a MLE estimator to data
emp_cov = EmpiricalCovariance().fit(X)
print(
    "Estimated covariance matrix:\nMCD (Robust):\n{}\nMLE:\n{}".format(
        robust_cov.covariance_, emp_cov.covariance_
    )
)
```
