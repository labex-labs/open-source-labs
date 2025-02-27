# Charger et préparer les données

Tout d'abord, nous allons charger l'ensemble de données sur le diabète et le préparer pour la modélisation. Nous utiliserons la fonction `load_diabetes` de scikit-learn pour charger l'ensemble de données dans deux tableaux, `X` et `y`.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True)
```
