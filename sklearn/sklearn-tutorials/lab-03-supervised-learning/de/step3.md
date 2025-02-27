# Support Vector Machines (SVMs)

In diesem Schritt werden wir das Konzept der Support Vector Machines (SVMs) erkunden und sehen, wie sie für Klassifizierungstasks verwendet werden können. SVMs versuchen, eine Hyperebene zu finden, die die Datenpunkte unterschiedlicher Klassen maximal trennt.

#### Erstelle und trainiere eine lineare SVM

```python
from sklearn import svm

svc = svm.SVC(kernel='linear')
svc.fit(iris_X_train, iris_y_train)
```

#### Erstelle und trainiere SVMs mit verschiedenen Kernen

```python
svc_poly = svm.SVC(kernel='poly', degree=3)
svc_rbf = svm.SVC(kernel='rbf')

svc_poly.fit(iris_X_train, iris_y_train)
svc_rbf.fit(iris_X_train, iris_y_train)
```
