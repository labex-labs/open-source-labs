# Charger le jeu de données

Tout d'abord, nous devons charger un jeu de données que nous pouvons utiliser pour entraîner notre modèle prédictif. Nous utiliserons le jeu de données Diabetes de scikit-learn, qui contient des informations sur des patients diabétiques.

```python
from sklearn.datasets import load_diabetes

# Charger le jeu de données Diabetes
diabetes = load_diabetes()

# Diviser les données en ensembles d'entraînement et de validation
X_train, X_val, y_train, y_val = train_test_split(diabetes.data, diabetes.target, random_state=0)
```
