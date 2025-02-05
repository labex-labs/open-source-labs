# 创建 RFE 对象并拟合数据

接下来，我们将创建一个 RFE 类的对象，并将数据拟合到该对象上。我们将使用具有线性核的支持向量分类器（SVC）作为估计器。我们将每次选择一个特征，并每次前进一个步骤。

```python
from sklearn.svm import SVC
from sklearn.feature_selection import RFE

svc = SVC(kernel="linear", C=1)
rfe = RFE(estimator=svc, n_features_to_select=1, step=1)
rfe.fit(X, y)
```
