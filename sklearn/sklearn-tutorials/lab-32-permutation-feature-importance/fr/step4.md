# Calculer l'importance des caractéristiques de permutation

Maintenant, nous allons calculer l'importance des caractéristiques de permutation à l'aide de la fonction `permutation_importance` de scikit-learn. Cette fonction prend en entrée le modèle entraîné, l'ensemble de validation et le nombre de fois où les caractéristiques doivent être permutées.

```python
from sklearn.inspection import permutation_importance

# Calculer l'importance des caractéristiques de permutation
result = permutation_importance(model, X_val, y_val, n_repeats=30, random_state=0)

# Afficher l'importance des caractéristiques
for i in result.importances_mean.argsort()[::-1]:
    if result.importances_mean[i] - 2 * result.importances_std[i] > 0:
        print(f"{diabetes.feature_names[i]}: {result.importances_mean[i]:.3f} +/- {result.importances_std[i]:.3f}")
```
