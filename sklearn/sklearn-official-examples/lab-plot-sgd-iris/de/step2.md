# Modell trainieren

Wir werden nun das SGDClassifier-Modell mit Hilfe der `fit()`-Methode auf dem Iris-Datensatz trainieren. Diese Methode nimmt die Eingabedaten und die Zielwerte als Eingabe und trainiert das Modell auf den angegebenen Daten.

```python
clf = SGDClassifier(alpha=0.001, max_iter=100).fit(X, y)
```
