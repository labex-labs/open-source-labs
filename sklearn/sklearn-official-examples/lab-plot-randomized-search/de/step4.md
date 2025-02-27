# Gitterverfahren zur Hyperparameteroptimierung

Wir werden das Gitterverfahren verwenden, um den Hyperparameterspace zu erkunden und die besten Hyperparameter für unser SVM-Modell zu finden.

```python
# Definieren Sie die Parameter, über die gesucht werden soll
param_grid = {
    "average": [True, False],
    "l1_ratio": np.linspace(0, 1, num=10),
    "alpha": np.power(10, np.arange(-2, 1, dtype=float)),
}

# Führen Sie das Gitterverfahren durch
grid_search = GridSearchCV(clf, param_grid=param_grid)

start = time()
grid_search.fit(X, y)

print(
    "GridSearchCV hat %.2f Sekunden für %d Kandidatenparameter-Einstellungen benötigt."
    % (time() - start, len(grid_search.cv_results_["params"]))
)

# Drucken Sie die Ergebnisse
report(grid_search.cv_results_)
```
