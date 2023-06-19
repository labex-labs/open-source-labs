# Implement LDA

Next, we will implement LDA using scikit-learn's `LinearDiscriminantAnalysis` class. We will create three classifiers:

- LDA with no shrinkage
- LDA with Ledoit-Wolf shrinkage
- LDA with OAS shrinkage

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.covariance import OAS

clf1 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage=None)
clf2 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
oa = OAS(store_precision=False, assume_centered=False)
clf3 = LinearDiscriminantAnalysis(solver="lsqr", covariance_estimator=oa)
```
