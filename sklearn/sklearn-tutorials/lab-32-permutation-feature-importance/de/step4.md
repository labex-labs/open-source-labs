# Berechne die Permutationsmerkmalwichtigkeit

Jetzt werden wir die Permutationsmerkmalwichtigkeit mit der Funktion `permutation_importance` aus scikit-learn berechnen. Diese Funktion nimmt als Eingabe das trainierte Modell, das Validierungsset und die Anzahl der Wiederholungen, bei denen die Merkmale permutiert werden sollen.

```python
from sklearn.inspection import permutation_importance

# Berechne die Permutationsmerkmalwichtigkeit
result = permutation_importance(model, X_val, y_val, n_repeats=30, random_state=0)

# Drucke die Merkmalswichtigkeiten
for i in result.importances_mean.argsort()[::-1]:
    if result.importances_mean[i] - 2 * result.importances_std[i] > 0:
        print(f"{diabetes.feature_names[i]}: {result.importances_mean[i]:.3f} +/- {result.importances_std[i]:.3f}")
```
