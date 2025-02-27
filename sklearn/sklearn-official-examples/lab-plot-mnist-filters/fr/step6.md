# Évaluer le modèle

Nous allons évaluer le MLPClassifier en calculant sa précision sur les ensembles d'entraînement et de test.

```python
print("Training set score: %f" % mlp.score(X_train, y_train))
print("Test set score: %f" % mlp.score(X_test, y_test))
```
