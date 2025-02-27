# Aufteilen der Daten

Wir werden die Daten in Trainings- und Testdatensätze aufteilen, indem wir die Funktion `train_test_split` aus scikit-learn verwenden.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
