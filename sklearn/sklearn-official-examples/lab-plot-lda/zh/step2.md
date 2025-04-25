# 实现线性判别分析（LDA）

接下来，我们将使用 scikit-learn 的`LinearDiscriminantAnalysis`类来实现 LDA。我们将创建三个分类器：

- 无收缩的 LDA
- 具有 Ledoit-Wolf 收缩的 LDA
- 具有 OAS 收缩的 LDA

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.covariance import OAS

clf1 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage=None)
clf2 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
oa = OAS(store_precision=False, assume_centered=False)
clf3 = LinearDiscriminantAnalysis(solver="lsqr", covariance_estimator=oa)
```
