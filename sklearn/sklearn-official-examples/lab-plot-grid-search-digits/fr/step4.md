# Ajuster le modèle et effectuer des prédictions

Nous allons ajuster le modèle et effectuer des prédictions sur l'ensemble d'évaluation.

```python
grid_search.fit(X_train, y_train)

# Les paramètres sélectionnés par la recherche sur grille avec notre stratégie personnalisée sont :
grid_search.best_params_

# Enfin, nous évaluons le modèle affiné sur l'ensemble d'évaluation non utilisé : l'objet
# `grid_search` **a été automatiquement réajusté** sur l'ensemble d'entraînement
# complet avec les paramètres sélectionnés par notre stratégie de réajustement personnalisée.
y_pred = grid_search.predict(X_test)
print(classification_report(y_test, y_pred))
```
