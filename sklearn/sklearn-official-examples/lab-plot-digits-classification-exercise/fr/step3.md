# Diviser le jeu de données en ensembles d'entraînement et de test

Ensuite, nous allons diviser le jeu de données en ensembles d'entraînement et de test à l'aide de la fonction `train_test_split` de scikit-learn. Nous utiliserons 90 % des données pour l'entraînement et 10 % pour les tests.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_digits, y_digits, test_size=0.1, random_state=42)
```
