# Ein-gegen-alle logistisches Regressionsmodell trainieren

Wir werden nun ein ein-gegen-alle logistisches Regressionsmodell mit den gleichen Parametern wie in Schritt 3 trainieren, jedoch mit der Mehrklassenoption auf `"ovr"` gesetzt. Anschließend werden wir die Trainingsgenauigkeit des Modells ausgeben.

```python
clf = LogisticRegression(
        solver="sag", max_iter=100, random_state=42, multi_class="ovr"
    ).fit(X, y)

print("training score : %.3f (%s)" % (clf.score(X, y), "ovr"))
```
