# Daten laden

```python
X, y = datasets.load_breast_cancer(return_X_y=True)
X, y = shuffle(X, y, random_state=42)
y_true = y.copy()
y[50:] = -1
total_samples = y.shape[0]
```

Der Datensatz `breast_cancer` wird geladen und gemischt. Anschließend kopieren wir die wahren Labels in `y_true` und entfernen alle Labels aus `y`, außer den ersten 50 Proben. Dies wird verwendet, um einen halbüberwachten Lernscenariobereich zu simulieren.
