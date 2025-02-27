# Diviser le jeu de données

Ensuite, nous divisons le jeu de données en ensembles d'entraînement et de test. Nous utiliserons 80 % des données pour l'entraînement et 20 % pour les tests.

```python
# Diviser les données en ensembles d'entraînement/tests
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Diviser les cibles en ensembles d'entraînement/tests
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```
