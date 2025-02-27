# Divisez l'ensemble de données en ensembles d'entraînement et de test

Pour évaluer les performances de notre modèle, nous devons diviser l'ensemble de données en un ensemble d'entraînement et un ensemble de test. Nous utiliserons la fonction `train_test_split` de la bibliothèque scikit-learn pour ce faire.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```
