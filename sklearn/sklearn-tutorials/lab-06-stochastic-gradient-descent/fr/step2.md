# Chargement des données

Ensuite, nous allons charger l'ensemble de données iris à partir de scikit-learn. Cet ensemble de données est un ensemble de données d'apprentissage automatique classique qui consiste en des mesures de fleurs d'iris, ainsi que leurs étiquettes d'espèces.

```python
iris = load_iris()
X = iris.data
y = iris.target
```
