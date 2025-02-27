# Modell auswerten

Wir werden den MLPClassifier indem wir seine Genauigkeit auf den Trainings- und Testsets berechnen, auswerten.

```python
print("Training set score: %f" % mlp.score(X_train, y_train))
print("Test set score: %f" % mlp.score(X_test, y_test))
```