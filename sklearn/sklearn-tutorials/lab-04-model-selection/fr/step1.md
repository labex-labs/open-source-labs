# Score et scores validés croisés

Les estimateurs dans scikit-learn exposent une méthode `score` qui peut être utilisée pour évaluer la qualité de l'ajustement du modèle ou de la prédiction sur de nouvelles données. Cette méthode renvoie un score, où une valeur plus élevée indique une meilleure performance.

```python
from sklearn import datasets, svm

# Chargez l'ensemble de données des chiffres
X_digits, y_digits = datasets.load_digits(return_X_y=True)

# Créez un classifieur SVM avec noyau linéaire
svc = svm.SVC(C=1, kernel='linear')

# Ajustez le classifieur sur les données d'entraînement et calculez le score sur les données de test
score = svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[-100:], y_digits[-100:])
```

Pour obtenir une mesure meilleure de la précision de prédiction, nous pouvons utiliser la validation croisée. La validation croisée consiste à diviser les données en plusieurs plis, en utilisant chaque pli comme ensemble de test et les plis restants comme ensembles d'entraînement. Ce processus est répété plusieurs fois, et les scores sont moyennés pour obtenir la performance globale.

```python
import numpy as np

# Divisez les données en 3 plis
X_folds = np.array_split(X_digits, 3)
y_folds = np.array_split(y_digits, 3)

# Effectuez la validation croisée
scores = []
for k in range(3):
    X_train = list(X_folds)
    X_test = X_train.pop(k)
    X_train = np.concatenate(X_train)
    y_train = list(y_folds)
    y_test = y_train.pop(k)
    y_train = np.concatenate(y_train)
    scores.append(svc.fit(X_train, y_train).score(X_test, y_test))

print(scores)
```
