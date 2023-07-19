# Support Vector Machines (SVMs)

In this step, we will explore the concept of support vector machines (SVMs) and how they can be used for classification tasks. SVMs aim to find a hyperplane that maximally separates the data points of different classes.

#### Create and Fit a Linear SVM

```python
from sklearn import svm

svc = svm.SVC(kernel='linear')
svc.fit(iris_X_train, iris_y_train)
```

#### Create and Fit SVMs with Different Kernels

```python
svc_poly = svm.SVC(kernel='poly', degree=3)
svc_rbf = svm.SVC(kernel='rbf')

svc_poly.fit(iris_X_train, iris_y_train)
svc_rbf.fit(iris_X_train, iris_y_train)
```
