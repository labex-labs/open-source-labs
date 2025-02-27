# Laden des Datensatzes

Wir werden den Digits-Datensatz mit `datasets.load_digits(return_X_y=True)` laden. Wir werden die Daten auch mithilfe von `StandardScaler().fit_transform(X)` standardisieren. Die Zielvariable wird binär sein, wobei 0-4 als 0 und 5-9 als 1 klassifiziert werden.

```python
X, y = datasets.load_digits(return_X_y=True)
X = StandardScaler().fit_transform(X)
y = (y > 4).astype(int)
```
