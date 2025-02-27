# GridSearchCV-Objekt definieren

Wir werden das GridSearchCV-Objekt definieren und das Modell anpassen.

```python
grid = GridSearchCV(
    pipe,
    cv=10,
    n_jobs=1,
    param_grid=param_grid,
    scoring="accuracy",
    refit=best_low_complexity,
)

grid.fit(X, y)
```
