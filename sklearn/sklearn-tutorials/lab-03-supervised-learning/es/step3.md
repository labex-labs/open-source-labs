# Máquinas de Vectores de Soporte (SVM)

En este paso, exploraremos el concepto de máquinas de vectores de soporte (SVM) y cómo se pueden utilizar para tareas de clasificación. Las SVM buscan encontrar un hiperplano que separe al máximo los puntos de datos de diferentes clases.

#### Crear y Ajustar una SVM Lineal

```python
from sklearn import svm

svc = svm.SVC(kernel='linear')
svc.fit(iris_X_train, iris_y_train)
```

#### Crear y Ajustar SVM con Diferentes Kernels

```python
svc_poly = svm.SVC(kernel='poly', degree=3)
svc_rbf = svm.SVC(kernel='rbf')

svc_poly.fit(iris_X_train, iris_y_train)
svc_rbf.fit(iris_X_train, iris_y_train)
```
