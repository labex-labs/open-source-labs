# Daten aufteilen

Wir werden den Datensatz in einen Trainingssatz und einen Testsatz aufteilen. Der Trainingssatz wird verwendet, um den SGD-Klassifikator (SGD classifier) zu trainieren, während der Testsatz zur Bewertung seiner Leistung dient.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
