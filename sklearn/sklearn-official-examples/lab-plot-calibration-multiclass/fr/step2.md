# Ajustement et étalonnage

Nous entraînons un classifieur à forêt aléatoire avec 25 estimateurs de base (arbres) sur les données d'entraînement et de validation concaténées (1000 échantillons). Il s'agit du classifieur non étalonné.

```python
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train_valid, y_train_valid)
```

Pour entraîner le classifieur étalonné, nous commençons avec le même classifieur à forêt aléatoire, mais l'entraînons en utilisant uniquement le sous-ensemble de données d'entraînement (600 échantillons), puis l'étalonnons, avec `méthode='sigmoid'`, en utilisant le sous-ensemble de données de validation (400 échantillons) dans un processus en deux étapes.

```python
from sklearn.calibration import CalibratedClassifierCV

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train, y_train)
cal_clf = CalibratedClassifierCV(clf, method="sigmoid", cv="prefit")
cal_clf.fit(X_valid, y_valid)
```
