# LDA implementieren

Als nächstes werden wir die LDA mit der `LinearDiscriminantAnalysis`-Klasse von scikit-learn implementieren. Wir werden drei Klassifizierer erstellen:

- LDA ohne Shrinkage
- LDA mit Ledoit-Wolf-Shrinkage
- LDA mit OAS-Shrinkage

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.covariance import OAS

clf1 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage=None)
clf2 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
oa = OAS(store_precision=False, assume_centered=False)
clf3 = LinearDiscriminantAnalysis(solver="lsqr", covariance_estimator=oa)
```
