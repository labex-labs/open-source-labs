# Datenaufbereitung

Als nächstes teilen wir unseren Datensatz auf, um 90 % für das Training zu verwenden und den Rest für das Testen zu belassen. Wir werden auch die Parameter des Regressionsmodells festlegen.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=13)

params = {
    "n_estimators": 500,
    "max_depth": 4,
    "min_samples_split": 5,
    "learning_rate": 0.01,
    "loss": "squared_error",
}
```
