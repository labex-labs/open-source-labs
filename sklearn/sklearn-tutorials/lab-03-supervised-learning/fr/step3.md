# Machines à vecteurs de support (SVM)

Dans cette étape, nous explorerons le concept de machines à vecteurs de support (SVM) et comment elles peuvent être utilisées pour les tâches de classification. Les SVM ont pour but de trouver un hyperplan qui sépare au maximum les points de données de différentes classes.

#### Créer et ajuster une SVM linéaire

```python
from sklearn import svm

svc = svm.SVC(kernel='linear')
svc.fit(iris_X_train, iris_y_train)
```

#### Créer et ajuster des SVM avec différents noyaux

```python
svc_poly = svm.SVC(kernel='poly', degree=3)
svc_rbf = svm.SVC(kernel='rbf')

svc_poly.fit(iris_X_train, iris_y_train)
svc_rbf.fit(iris_X_train, iris_y_train)
```
