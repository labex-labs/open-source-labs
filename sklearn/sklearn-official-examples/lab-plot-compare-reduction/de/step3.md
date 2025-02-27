# Erstellen eines GridSearchCV-Objekts und Anpassen der Daten

Wir werden ein `GridSearchCV`-Objekt mit der Pipeline und dem Parameter-Grid erstellen, die wir im vorherigen Schritt definiert haben. Anschließend werden wir die Daten an das Objekt anpassen.

```python
grid = GridSearchCV(pipe, n_jobs=1, param_grid=param_grid)
grid.fit(X, y)
```
