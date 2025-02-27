# Teilen des Datensatzes

Wir werden den Datensatz in Trainings- und Testsets aufteilen, wobei die ersten 3000 Proben zum Training und die verbleibenden Proben zum Testen verwendet werden.

```python
n_split = 3000
X_train, X_test = X[:n_split], X[n_split:]
y_train, y_test = y[:n_split], y[n_split:]
```
