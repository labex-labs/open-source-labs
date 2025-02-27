# Faire des prédictions

Une fois que le classifieur est entraîné, nous pouvons l'utiliser pour faire des prédictions sur de nouvelles données. Ici, nous allons l'utiliser pour prédire les classes cibles pour l'ensemble de test.

```python
y_pred = clf.predict(X_test)
```
