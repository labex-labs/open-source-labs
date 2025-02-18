# Génération des données

Dans cette étape, nous allons générer les données pour entraîner et tester le classifieur SVM. Nous allons générer 300 points de données aléatoires avec deux caractéristiques. La cible à prédire est un OU exclusif (XOR) des entrées.

```python
np.random.seed(0)
X = np.random.randn(300, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
```
