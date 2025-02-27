# Multinomiale logistische Regressionsmodell trainieren

Wir werden nun ein multinomiales logistisches Regressionsmodell mit der Funktion `LogisticRegression` aus scikit-learn trainieren. Wir werden den Solver auf `"sag"` setzen, die maximale Anzahl an Iterationen auf 100, den Zufallszustand auf 42 und die Mehrklassenoption auf `"multinomial"`. Anschließend werden wir die Trainingsgenauigkeit des Modells ausgeben.

```python
clf = LogisticRegression(
        solver="sag", max_iter=100, random_state=42, multi_class="multinomial"
    ).fit(X, y)

print("training score : %.3f (%s)" % (clf.score(X, y), "multinomial"))
```
