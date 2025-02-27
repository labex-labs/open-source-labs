# Prédiction sur de nouvelles données

Nous allons utiliser à la fois l'arbre de décision aléatoire pour la régression et le multi-output regressor pour effectuer des prédictions sur nos données de test.

```python
y_rf = regr_rf.predict(X_test)
y_multirf = regr_multirf.predict(X_test)
```
