# Recherche sur grille

La recherche sur grille est une technique qui peut être utilisée pour trouver la meilleure combinaison de valeurs de paramètres pour un estimateur. Elle consiste à spécifier une grille de valeurs de paramètres, à ajuster l'estimateur sur les données d'entraînement pour chaque combinaison de paramètres, et à sélectionner les paramètres qui donnent le score de validation croisée le plus élevé.

```python
from sklearn.model_selection import GridSearchCV

# Définissez une grille de valeurs de paramètres
Cs = np.logspace(-6, -1, 10)

# Créez un objet GridSearchCV avec le classifieur SVM et la grille de paramètres
clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), n_jobs=-1)

# Ajustez l'objet GridSearchCV sur les données d'entraînement
clf.fit(X_digits[:1000], y_digits[:1000])

print(clf.best_score_)
print(clf.best_estimator_.C)
```
