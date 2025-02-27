# Évaluer les performances

Enfin, nous allons évaluer les performances du classifieur en calculant la précision de ses prédictions sur l'ensemble de test.

```python
accuracy = accuracy_score(y_test, y_pred)
print("Précision :", accuracy)
```
