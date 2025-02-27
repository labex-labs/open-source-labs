# Chargez l'ensemble de données

Ensuite, nous allons charger l'ensemble de données Iris. Cet ensemble de données contient des informations sur quatre caractéristiques de trois espèces différentes de fleurs Iris. Nous allons utiliser cet ensemble de données pour entraîner notre classifieur d'arbres de décision.

```python
# Chargez l'ensemble de données Iris
iris = load_iris()
X = iris.data
y = iris.target
```
