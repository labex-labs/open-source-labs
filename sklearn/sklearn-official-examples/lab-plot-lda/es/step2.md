# Implementar LDA

A continuación, implementaremos el LDA utilizando la clase `LinearDiscriminantAnalysis` de scikit-learn. Crearemos tres clasificadores:

- LDA sin encogimiento
- LDA con encogimiento Ledoit-Wolf
- LDA con encogimiento OAS

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.covariance import OAS

clf1 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage=None)
clf2 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
oa = OAS(store_precision=False, assume_centered=False)
clf3 = LinearDiscriminantAnalysis(solver="lsqr", covariance_estimator=oa)
```
