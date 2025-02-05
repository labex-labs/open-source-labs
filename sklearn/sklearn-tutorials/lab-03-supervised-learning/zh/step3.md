# 支持向量机（SVM）

在这一步中，我们将探索支持向量机（SVM）的概念，以及它们如何用于分类任务。SVM旨在找到一个超平面，将不同类别的数据点最大程度地分开。

#### 创建并拟合线性SVM

```python
from sklearn import svm

svc = svm.SVC(kernel='linear')
svc.fit(iris_X_train, iris_y_train)
```

#### 创建并拟合具有不同核的SVM

```python
svc_poly = svm.SVC(kernel='poly', degree=3)
svc_rbf = svm.SVC(kernel='rbf')

svc_poly.fit(iris_X_train, iris_y_train)
svc_rbf.fit(iris_X_train, iris_y_train)
```
