# Chargez les données

Ensuite, nous chargeons le jeu de données iris à partir de Scikit-learn et sélectionnons seulement les deux premières caractéristiques pour les besoins de visualisation.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target
```
