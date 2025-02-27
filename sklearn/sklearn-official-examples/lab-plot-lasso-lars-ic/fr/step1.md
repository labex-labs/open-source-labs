# Charger les données

Nous allons charger le jeu de données diabetes de scikit-learn en utilisant la méthode load_diabetes.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True, as_frame=True)
```
