# Implémenter l'ALD

Ensuite, nous allons implémenter l'ALD en utilisant la classe `LinearDiscriminantAnalysis` de scikit-learn. Nous allons créer trois classifieurs :

- ALD sans réduction
- ALD avec réduction Ledoit-Wolf
- ALD avec réduction OAS

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.covariance import OAS

clf1 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage=None)
clf2 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
oa = OAS(store_precision=False, assume_centered=False)
clf3 = LinearDiscriminantAnalysis(solver="lsqr", covariance_estimator=oa)
```
