# Teilen der Daten in Trainings- und Testsets

Wir werden unsere Daten mit der `train_test_split`-Funktion von scikit-learn in einen Trainingssatz von 400 und einen Testsatz von 200 teilen.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=400, test_size=200, random_state=4)
```
