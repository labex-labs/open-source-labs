# Entraînement et sélection du modèle

Nous allons créer l'objet RFECV et calculer les scores validés croisés. La stratégie de notation "accuracy" optimise la proportion d'échantillons correctement classés. Nous utiliserons la régression logistique comme estimateur et la validation croisée stratifiée k-fold avec 5 plis.

```python
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression

min_features_to_select = 1  # Nombre minimum de caractéristiques à considérer
clf = LogisticRegression()
cv = StratifiedKFold(5)

rfecv = RFECV(
    estimator=clf,
    step=1,
    cv=cv,
    scoring="accuracy",
    min_features_to_select=min_features_to_select,
    n_jobs=2,
)
rfecv.fit(X, y)

print(f"Nombre optimal de caractéristiques: {rfecv.n_features_}")
```
