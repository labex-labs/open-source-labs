# Validation croisée non imbriquée (Non-Nested Cross-Validation)

Nous utilisons la validation croisée non imbriquée pour ajuster les hyperparamètres et évaluer les performances du modèle. La fonction `GridSearchCV` effectue une recherche exhaustive sur les valeurs de paramètres spécifiées pour un estimateur. Nous utilisons une validation croisée en 4 plis (4-fold cross-validation).

```python
from sklearn.model_selection import GridSearchCV

# Non_nested parameter search and scoring
clf = GridSearchCV(estimator=svm, param_grid=p_grid, cv=4)
clf.fit(X_iris, y_iris)
non_nested_score = clf.best_score_
```
