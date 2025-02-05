# 设置支持向量机分类器

我们将设置一个使用径向基函数（RBF）核的支持向量机分类器。支持向量机是一种监督学习算法，它寻找能将数据分隔到不同类别的最优超平面。

```python
from sklearn.svm import SVC

# 设置支持向量机分类器
rbf_svc = (SVC(kernel="rbf", gamma=0.5).fit(X, y), y, "SVC with rbf kernel")
```
