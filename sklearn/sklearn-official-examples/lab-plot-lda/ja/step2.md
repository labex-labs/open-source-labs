# LDAを実装する

次に、scikit - learnの`LinearDiscriminantAnalysis`クラスを使用してLDAを実装します。3つの分類器を作成します。

- 収縮なしのLDA
- Ledoit - Wolf収縮を伴うLDA
- OAS収縮を伴うLDA

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.covariance import OAS

clf1 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage=None)
clf2 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
oa = OAS(store_precision=False, assume_centered=False)
clf3 = LinearDiscriminantAnalysis(solver="lsqr", covariance_estimator=oa)
```
