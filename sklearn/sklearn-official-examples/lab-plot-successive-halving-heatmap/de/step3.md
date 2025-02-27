# Führen Sie Successive Halving durch

Wir werden nun eine Parameter-Suche mit Successive Halving auf dem gleichen SVC-Modell und Datensatz durchführen, der in Schritt 2 verwendet wurde.

```python
tic = time()
gsh = HalvingGridSearchCV(
    estimator=clf, param_grid=param_grid, factor=2, random_state=rng
)
gsh.fit(X, y)
gsh_time = time() - tic
```
