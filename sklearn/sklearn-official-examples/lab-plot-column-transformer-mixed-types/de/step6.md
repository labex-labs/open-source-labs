# Teile die Daten auf

In diesem Schritt teilen wir unsere Daten in Trainings- und Testsets auf, indem wir `train_test_split` verwenden.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
```
