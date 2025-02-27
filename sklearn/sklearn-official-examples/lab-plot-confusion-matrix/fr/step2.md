# Charger les données

Nous utiliserons l'ensemble de données iris de scikit-learn. L'ensemble de données contient 150 échantillons, chacun avec quatre caractéristiques et une étiquette cible.

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names
```
