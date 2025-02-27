# Das Modell auswerten

Wir bewerten den MLPClassifier, indem wir seine Genauigkeit (Accuracy) auf den Trainings- und Testsets berechnen.

```python
print("Training set score: %f" % mlp.score(X_train, y_train))
print("Test set score: %f" % mlp.score(X_test, y_test))
```
