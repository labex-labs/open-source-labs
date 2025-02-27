# Erstellen einer Instanz des Logistischen Regressionsklassifizierers und Anpassen der Daten

Wir werden eine Instanz des Logistischen Regressionsklassifizierers erstellen und die Daten anpassen.

```python
# Erstellt eine Instanz des Logistischen Regressionsklassifizierers und passt die Daten an.
logreg = LogisticRegression(C=1e5)
logreg.fit(X, Y)
```
