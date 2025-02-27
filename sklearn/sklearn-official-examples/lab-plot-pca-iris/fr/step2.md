# Charger l'ensemble de données

Ensuite, nous allons charger l'ensemble de données Iris à l'aide de la fonction `load_iris()` de scikit-learn. Nous séparerons ensuite les variables de caractéristiques (X) et de cible (y).

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
```
