# Générer des prédictions validées croisées

Nous allons utiliser la fonction `cross_val_predict` de scikit-learn pour générer des prédictions validées croisées.

```python
from sklearn.model_selection import cross_val_predict

y_pred = cross_val_predict(lr, X, y, cv=10)
```
