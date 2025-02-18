# Définir le modèle

Nous utilisons un classifieur à vecteurs de support (Support Vector Classifier) avec un noyau de fonction de base radiale (radial basis function kernel).

```python
from sklearn.svm import SVC

# We will use a Support Vector Classifier with "rbf" kernel
svm = SVC(kernel="rbf")
```
