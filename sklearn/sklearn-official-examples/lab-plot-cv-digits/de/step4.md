# Führe Kreuzvalidierung durch und protokolliere die Ergebnisse

Für jeden Wert von C führen wir eine 10-fache Kreuzvalidierung durch und protokollieren den Mittelwert und die Standardabweichung der Scores.

```python
from sklearn.model_selection import cross_val_score

scores = list()
scores_std = list()
for C in C_s:
    svc.C = C
    this_scores = cross_val_score(svc, X, y, n_jobs=1)
    scores.append(np.mean(this_scores))
    scores_std.append(np.std(this_scores))
```
