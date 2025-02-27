# MCD- und MLE-Kovarianzschätzer an die Daten anpassen

Wir werden die auf MCD und MLE basierenden Kovarianzschätzer an unsere Daten anpassen und die geschätzten Kovarianzmatrizen ausgeben. Beachten Sie, dass die geschätzte Varianz von Merkmal 2 mit dem auf MLE basierenden Schätzer (7,5) viel höher ist als die des robusten MCD-Schätzers (1,2). Dies zeigt, dass der robuste MCD-basierte Schätzer viel widerstandsfähiger gegenüber den Ausreißerproben ist, die so konzipiert wurden, dass Merkmal 2 eine viel größere Varianz hat.

```python
from sklearn.covariance import EmpiricalCovariance, MinCovDet

# passe einen robusten MCD-Schätzer an die Daten an
robust_cov = MinCovDet().fit(X)
# passe einen MLE-Schätzer an die Daten an
emp_cov = EmpiricalCovariance().fit(X)
print(
    "Geschätzte Kovarianzmatrix:\nMCD (Robust):\n{}\nMLE:\n{}".format(
        robust_cov.covariance_, emp_cov.covariance_
    )
)
```
