# Évaluer le modèle

Nous allons maintenant évaluer le modèle entraîné à l'aide de l'ensemble de validation. La métrique d'évaluation utilisée ici est le coefficient de détermination R².

```python
# Évaluer le modèle sur l'ensemble de validation
score = model.score(X_val, y_val)
print("Score de validation :", score)
```
