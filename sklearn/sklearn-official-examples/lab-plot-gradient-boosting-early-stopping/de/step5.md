# Vergleiche die Scores mit und ohne Early Stopping

Wir werden nun die Scores der beiden Modelle vergleichen.

```python
score_gb.append(gb.score(X_test, y_test))
score_gbes.append(gbes.score(X_test, y_test))
```
