# Daten aufteilen

Wir werden den Datensatz in einen Trainingssatz und einen Testsatz aufteilen. Der Trainingssatz wird verwendet, um den SGD-Klassifizierer zu trainieren, während der Testsatz verwendet wird, um seine Leistung zu evaluieren.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```