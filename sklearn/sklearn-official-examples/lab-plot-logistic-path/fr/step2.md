# Calculer la trajectoire de régularisation

Nous allons calculer la trajectoire de régularisation en entraînant des modèles de régression logistique pénalisés L1 avec différentes forces de régularisation. Nous utiliserons le solveur liblinear, qui peut optimiser efficacement la perte de régression logistique avec une pénalité L1. Nous allons définir une valeur basse pour la tolérance pour nous assurer que le modèle a convergé avant de collecter les coefficients. Nous utiliserons également warm_start=True, ce qui signifie que les coefficients des modèles sont réutilisés pour initialiser l'ajustement du prochain modèle afin d'accélérer le calcul de la trajectoire complète.

```python
import numpy as np
from sklearn import linear_model
from sklearn.svm import l1_min_c

cs = l1_min_c(X, y, loss="log") * np.logspace(0, 10, 16)

clf = linear_model.LogisticRegression(
    penalty="l1",
    solver="liblinear",
    tol=1e-6,
    max_iter=int(1e6),
    warm_start=True,
    intercept_scaling=10000.0,
)
coefs_ = []
for c in cs:
    clf.set_params(C=c)
    clf.fit(X, y)
    coefs_.append(clf.coef_.ravel().copy())

coefs_ = np.array(coefs_)
```
