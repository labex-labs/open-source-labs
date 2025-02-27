# Configurer le classifieur SVM

Nous allons configurer un classifieur SVM avec un noyau de fonction de base radiale (RBF). Le SVM est un algorithme d'apprentissage supervisé qui trouve l'hyperplan optimal qui sépare les données en différentes classes.

```python
from sklearn.svm import SVC

# Configurer le classifieur SVM
rbf_svc = (SVC(kernel="rbf", gamma=0.5).fit(X, y), y, "SVC avec noyau rbf")
```
