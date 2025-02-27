# Daten aufteilen

Wir teilen den Datensatz in einen Trainingssatz und einen Testsatz auf, indem wir die Funktion `train_test_split` verwenden.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.7)
```
