# Créer l'objet RFE et ajuster les données

Ensuite, nous allons créer un objet de la classe RFE et l'ajuster aux données. Nous utiliserons un classifieur à vecteurs de support (SVC) avec un noyau linéaire comme estimateur. Nous sélectionnerons une caractéristique à la fois et prendrons une étape à la fois.

```python
from sklearn.svm import SVC
from sklearn.feature_selection import RFE

svc = SVC(kernel="linear", C=1)
rfe = RFE(estimator=svc, n_features_to_select=1, step=1)
rfe.fit(X, y)
```
