# Entraînement d'un modèle d'apprentissage automatique

Maintenant que nous avons préparé l'ensemble de données, nous pouvons entraîner un modèle d'apprentissage automatique sur les données d'entraînement. Dans cet exemple, nous allons utiliser un algorithme de Machine à Vecteurs de Support (SVM) :

```python
from sklearn.svm import SVC

# Crée le classifieur SVM
clf = SVC(kernel='linear')

# Entraîne le classifieur sur les données d'entraînement
clf.fit(X_train, y_train)
```
