# サポートベクターマシン (SVM)

このステップでは、サポートベクターマシン (SVM) の概念と、分類タスクにどのように使用できるかを探ります。SVM は、異なるクラスのデータポイントを最大限に分離する超平面を見つけることを目的としています。

#### 線形 SVM を作成して適合させる

```python
from sklearn import svm

svc = svm.SVC(kernel='linear')
svc.fit(iris_X_train, iris_y_train)
```

#### 異なるカーネルを持つ SVM を作成して適合させる

```python
svc_poly = svm.SVC(kernel='poly', degree=3)
svc_rbf = svm.SVC(kernel='rbf')

svc_poly.fit(iris_X_train, iris_y_train)
svc_rbf.fit(iris_X_train, iris_y_train)
```
