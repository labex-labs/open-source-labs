# Das Modell trainieren

Wir werden jetzt das LOF-Modell mit den Trainingsdaten trainieren. Wir setzen die Anzahl der Nachbarn auf 20 und die Neuheit (novelty) auf `true`. Wir setzen auch die Kontamination (contamination) auf 0,1.

```python
clf = LocalOutlierFactor(n_neighbors=20, novelty=True, contamination=0.1)
clf.fit(X_train)
```
