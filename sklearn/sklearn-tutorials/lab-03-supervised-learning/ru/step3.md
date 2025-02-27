# Методы опорных векторов (SVM)

В этом разделе мы изучим концепцию методов опорных векторов (SVM) и узнаем, как их можно использовать для задач классификации. SVM旨在找到一个超平面，该超平面能最大程度地分隔不同类别的数据点。

#### Создание и обучение линейного SVM

```python
from sklearn import svm

svc = svm.SVC(kernel='linear')
svc.fit(iris_X_train, iris_y_train)
```

#### Создание и обучение SVM с разными ядрами

```python
svc_poly = svm.SVC(kernel='poly', degree=3)
svc_rbf = svm.SVC(kernel='rbf')

svc_poly.fit(iris_X_train, iris_y_train)
svc_rbf.fit(iris_X_train, iris_y_train)
```
