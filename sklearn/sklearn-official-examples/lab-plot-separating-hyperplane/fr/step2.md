# Ajuster le modèle SVM

Ensuite, nous allons ajuster le modèle SVM à notre ensemble de données en utilisant un noyau linéaire et un paramètre de régularisation de 1000. Nous utiliserons la fonction `svm.SVC()` de scikit-learn pour créer le classifieur SVM.

```python
from sklearn import svm

# ajuster le modèle SVM
clf = svm.SVC(kernel="linear", C=1000)
clf.fit(X, y)
```
