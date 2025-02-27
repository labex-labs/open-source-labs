# Tracez la courbe de validation

Maintenant, traçons la courbe de validation à l'aide de la fonction `validation_curve`. Nous utiliserons l'estimateur `Ridge` et ferons varier l'hyperparamètre `alpha` sur une plage de valeurs.

```python
param_range = np.logspace(-7, 3, 3)
train_scores, valid_scores = validation_curve(
    Ridge(), X, y, param_name="alpha", param_range=param_range, cv=5)
```
