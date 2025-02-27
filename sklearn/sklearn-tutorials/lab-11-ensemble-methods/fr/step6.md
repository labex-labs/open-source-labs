# Ajuster un classifieur à forêt aléatoire

Ensuite, nous allons ajuster un classifieur à forêt aléatoire sur les données d'entraînement. Le classifieur à forêt aléatoire est également une méthode d'ensemble qui utilise l'échantillonnage bootstrap pour créer plusieurs arbres de décision, mais il ajoute également une aléatoire supplémentaire en considérant seulement un sous-ensemble de caractéristiques à chaque division.

```python
random_forest = RandomForestClassifier(n_estimators=10)
random_forest.fit(X_train, y_train)
```
