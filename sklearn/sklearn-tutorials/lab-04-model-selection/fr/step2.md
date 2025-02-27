# Générateurs de validation croisée

Scikit-learn fournit une collection de classes qui peuvent être utilisées pour générer des indices d'entraînement/tests pour les stratégies de validation croisée populaires. Ces classes ont une méthode `split` qui accepte l'ensemble de données d'entrée et renvoie les indices d'ensemble d'entraînement/tests pour chaque itération du processus de validation croisée.

```python
from sklearn.model_selection import KFold

# Divisez les données en K plis en utilisant la validation croisée KFold
k_fold = KFold(n_splits=5)
for train_indices, test_indices in k_fold.split(X_digits):
    print(f'Train: {train_indices} | test: {test_indices}')
```

La fonction d'aide `cross_val_score` peut être utilisée pour calculer directement le score de validation croisée. Elle divise les données en ensembles d'entraînement et de test pour chaque itération de la validation croisée, entraîne l'estimateur sur l'ensemble d'entraînement et calcule le score sur la base de l'ensemble de test.

```python
from sklearn.model_selection import cross_val_score

# Calculez le score de validation croisée pour le classifieur SVM
scores = cross_val_score(svc, X_digits, y_digits, cv=k_fold, n_jobs=-1)
print(scores)
```
