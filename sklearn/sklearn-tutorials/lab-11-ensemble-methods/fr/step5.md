# Évaluer le classifieur Bagging

Évaluons le classifieur Bagging en calculant le score d'exactitude sur les données de test en utilisant la méthode `score`.

```python
accuracy = bagging.score(X_test, y_test)
print(f"Précision du classifieur Bagging : {accuracy}")
```
