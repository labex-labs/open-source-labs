# Ajustar el modelo de SVM

A continuación, ajustaremos el modelo de SVM a nuestro conjunto de datos usando un kernel lineal y un parámetro de regularización de 1000. Usaremos la función `svm.SVC()` de scikit-learn para crear el clasificador de SVM.

```python
from sklearn import svm

# fit the SVM model
clf = svm.SVC(kernel="linear", C=1000)
clf.fit(X, y)
```
