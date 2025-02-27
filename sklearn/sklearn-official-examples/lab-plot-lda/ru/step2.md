# Реализация LDA

Далее мы реализуем LDA с использованием класса `LinearDiscriminantAnalysis` из scikit - learn. Мы создадим три классификатора:

- LDA без сжатия
- LDA с сжатием Ледоита-Вольфа
- LDA с сжатием OAS

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.covariance import OAS

clf1 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage=None)
clf2 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
oa = OAS(store_precision=False, assume_centered=False)
clf3 = LinearDiscriminantAnalysis(solver="lsqr", covariance_estimator=oa)
```
