# Évaluer le classifieur à forêt aléatoire

Évaluons le classifieur à forêt aléatoire en calculant le score d'exactitude sur les données de test.

```python
accuracy = random_forest.score(X_test, y_test)
print(f"Précision du classifieur à forêt aléatoire : {accuracy}")
```
