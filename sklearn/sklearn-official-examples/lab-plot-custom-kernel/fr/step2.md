# Charger les données

Dans cette étape, nous allons charger l'ensemble de données iris à l'aide du module datasets de scikit-learn. Nous sélectionnerons les deux premières caractéristiques de l'ensemble de données et nous les assignerons à la variable X. Nous assignerons également la variable cible à Y.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
Y = iris.target
```
