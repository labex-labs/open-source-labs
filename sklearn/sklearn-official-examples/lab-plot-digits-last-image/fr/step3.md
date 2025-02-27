# Préparation de l'ensemble de données pour l'apprentissage automatique

Avant de pouvoir entraîner un modèle d'apprentissage automatique sur l'ensemble de données, nous devons préparer les données en les divisant en ensembles d'entraînement et de test. Nous pouvons le faire à l'aide de la fonction `train_test_split` de scikit-learn :

```python
from sklearn.model_selection import train_test_split

# Divise l'ensemble de données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)
```
