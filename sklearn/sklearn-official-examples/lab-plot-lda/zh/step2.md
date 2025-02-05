# 实现线性判别分析（LDA）

接下来，我们将使用scikit-learn的`LinearDiscriminantAnalysis`类来实现LDA。我们将创建三个分类器：

- 无收缩的LDA
- 具有Ledoit-Wolf收缩的LDA
- 具有OAS收缩的LDA

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.covariance import OAS

clf1 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage=None)
clf2 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
oa = OAS(store_precision=False, assume_centered=False)
clf3 = LinearDiscriminantAnalysis(solver="lsqr", covariance_estimator=oa)
```
