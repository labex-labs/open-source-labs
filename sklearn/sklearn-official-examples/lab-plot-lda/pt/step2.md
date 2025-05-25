# Implementar LDA

Em seguida, implementaremos LDA usando a classe `LinearDiscriminantAnalysis` do scikit-learn. Criaremos três classificadores:

- LDA sem encolhimento
- LDA com encolhimento Ledoit-Wolf
- LDA com encolhimento OAS

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.covariance import OAS

clf1 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage=None)
clf2 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
oa = OAS(store_precision=False, assume_centered=False)
clf3 = LinearDiscriminantAnalysis(solver="lsqr", covariance_estimator=oa)
```
