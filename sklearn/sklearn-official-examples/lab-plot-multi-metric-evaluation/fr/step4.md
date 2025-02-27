# Effectuer la recherche sur grille

Dans cette étape, nous allons utiliser la fonction GridSearchCV pour effectuer la recherche sur grille. Nous allons chercher les meilleurs hyperparamètres pour le paramètre min_samples_split du modèle DecisionTreeClassifier.

```python
gs = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid={"min_samples_split": range(2, 403, 20)},
    scoring=scoring,
    refit="AUC",
    n_jobs=2,
    return_train_score=True,
)
gs.fit(X, y)
results = gs.cv_results_
```
