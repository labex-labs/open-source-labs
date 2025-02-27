# Daten aufteilen

Wir werden den Datensatz in einen Trainingssatz und einen Testsatz aufteilen. Der Trainingssatz wird verwendet, um das Modell zu trainieren, und der Testsatz wird verwendet, um die Leistung des Modells zu evaluieren.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```
