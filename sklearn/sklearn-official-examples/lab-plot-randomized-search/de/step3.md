# Zufällige Suche zur Hyperparameteroptimierung

Wir werden die zufällige Suche verwenden, um den Hyperparameterspace zu erkunden und die besten Hyperparameter für unser SVM-Modell zu finden.

```python
# Definieren Sie die Parameter und Verteilungen, aus denen zu ziehen
param_dist = {
    "average": [True, False],
    "l1_ratio": stats.uniform(0, 1),
    "alpha": stats.loguniform(1e-2, 1e0),
}

# Führen Sie die zufällige Suche durch
n_iter_search = 15
random_search = RandomizedSearchCV(
    clf, param_distributions=param_dist, n_iter=n_iter_search
)

start = time()
random_search.fit(X, y)
print(
    "RandomizedSearchCV hat %.2f Sekunden für %d Kandidatenparameter-Einstellungen benötigt."
    % ((time() - start), n_iter_search)
)

# Drucken Sie die Ergebnisse
report(random_search.cv_results_)
```
