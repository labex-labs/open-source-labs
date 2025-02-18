# Validation croisée imbriquée (Nested Cross-Validation)

Nous utilisons la validation croisée imbriquée pour estimer l'erreur de généralisation du modèle et de ses hyperparamètres. Dans la boucle interne, nous effectuons une recherche sur grille (grid search) pour trouver les meilleurs hyperparamètres pour chaque ensemble d'entraînement. Dans la boucle externe, nous évaluons les performances du modèle sur l'ensemble de test.

```python
from sklearn.model_selection import KFold, cross_val_score

# Number of random trials
NUM_TRIALS = 30

# Arrays to store scores
non_nested_scores = np.zeros(NUM_TRIALS)
nested_scores = np.zeros(NUM_TRIALS)

# Loop for each trial
for i in range(NUM_TRIALS):
    # Choose cross-validation techniques for the inner and outer loops,
    # independently of the dataset.
    inner_cv = KFold(n_splits=4, shuffle=True, random_state=i)
    outer_cv = KFold(n_splits=4, shuffle=True, random_state=i)

    # Nested CV with parameter optimization
    clf = GridSearchCV(estimator=svm, param_grid=p_grid, cv=inner_cv)
    nested_score = cross_val_score(clf, X=X_iris, y=y_iris, cv=outer_cv)
    nested_scores[i] = nested_score.mean()

score_difference = non_nested_score - nested_scores.mean()
```
