# Den Datensatz aufteilen

Wir werden den Datensatz in einen Trainings- und einen Testdatensatz von jeweils 50% unter Verwendung der `train_test_split()`-Methode aus `sklearn.model_selection` aufteilen.

```python
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)
```
