# Entraînement et test

Nous allons ajuster notre pipeline sur les données d'entraînement et l'utiliser pour prédire les sujets pour `X_test`. Les métriques de performance de notre pipeline sont ensuite affichées.

```python
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print("Classification report:\n\n{}".format(classification_report(y_test, y_pred)))
```
