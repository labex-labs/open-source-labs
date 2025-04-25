# LDA を実装する

次に、scikit - learn の`LinearDiscriminantAnalysis`クラスを使用して LDA を実装します。3 つの分類器を作成します。

- 収縮なしの LDA
- Ledoit - Wolf 収縮を伴う LDA
- OAS 収縮を伴う LDA

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.covariance import OAS

clf1 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage=None)
clf2 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
oa = OAS(store_precision=False, assume_centered=False)
clf3 = LinearDiscriminantAnalysis(solver="lsqr", covariance_estimator=oa)
```
