# Charger le jeu de données Digits

Nous allons commencer par charger le jeu de données Digits à l'aide de la fonction `load_digits` de scikit-learn. Cette fonction renvoie deux tableaux : `X_digits` contenant les données d'entrée et `y_digits` contenant les étiquettes cibles.

```python
from sklearn import datasets

X_digits, y_digits = datasets.load_digits(return_X_y=True)
```
