# Charger les données

Nous utiliserons le jeu de données du cancer du sein de scikit-learn. Ce jeu de données a 30 caractéristiques et une variable cible binaire indiquant si un patient a un cancer malin ou bénin.

```python
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
```
